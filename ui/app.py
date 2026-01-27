"""
North Star for High-Conflict Cases
Flask Web Application

A local web interface that uses Kiro's architecture (steering docs + custom prompts)
powered by Claude API for non-technical users.

This provides the same analysis as the Kiro CLI but with a compassionate UI
designed for parents in crisis situations.
"""

import os
import sys
from pathlib import Path
from flask import Flask, render_template, request, jsonify, send_file
from werkzeug.utils import secure_filename
from dotenv import load_dotenv
from anthropic import Anthropic

# Load environment variables
load_dotenv(Path(__file__).resolve().parent.parent / '.env')

app = Flask(__name__)

# Configuration
BASE_DIR = Path(__file__).resolve().parent.parent
UPLOAD_FOLDER = BASE_DIR / 'uploads'
OUTPUT_FOLDER = BASE_DIR / 'outputs'
KIRO_DIR = BASE_DIR / '.kiro'
ALLOWED_EXTENSIONS = {'txt', 'md'}
MAX_CONTENT_LENGTH = 5 * 1024 * 1024  # 5MB max (~10 pages)

# Ensure directories exist
UPLOAD_FOLDER.mkdir(exist_ok=True)
OUTPUT_FOLDER.mkdir(exist_ok=True)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = MAX_CONTENT_LENGTH

# Initialize Anthropic client
api_key = os.getenv('ANTHROPIC_API_KEY')
if not api_key:
    print("ERROR: ANTHROPIC_API_KEY not found in .env file")
    sys.exit(1)

client = Anthropic(api_key=api_key)


def allowed_file(filename):
    """Check if file extension is allowed."""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def load_kiro_context():
    """Load Kiro steering documents and prompts as system context."""
    context_parts = []

    # Load steering documents
    steering_files = ['product.md', 'tech.md', 'structure.md']
    for filename in steering_files:
        filepath = KIRO_DIR / 'steering' / filename
        if filepath.exists():
            content = filepath.read_text(encoding='utf-8')
            context_parts.append(f"# Steering Document: {filename}\n\n{content}\n\n")

    # Load the analyze.md orchestrator prompt
    analyze_prompt = KIRO_DIR / 'prompts' / 'analyze.md'
    if analyze_prompt.exists():
        content = analyze_prompt.read_text(encoding='utf-8')
        context_parts.append(f"# Main Analysis Prompt\n\n{content}\n\n")

    # Load pattern taxonomy
    pattern_taxonomy = BASE_DIR / 'reference' / 'child-impact-patterns.md'
    if pattern_taxonomy.exists():
        content = pattern_taxonomy.read_text(encoding='utf-8')
        context_parts.append(f"# Pattern Taxonomy\n\n{content}\n\n")

    return "\n".join(context_parts)


def analyze_document_with_claude(document_content, filename):
    """
    Analyze a document using Claude API with Kiro's prompts and steering docs.
    Returns the three generated output summaries.
    """
    # Load Kiro context
    system_context = load_kiro_context()

    # Create the user message with the document
    user_message = f"""I have a custody documentation file to analyze using the North Star system.

**Document filename:** {filename}

**Document content:**

{document_content}

---

Please execute the full three-step analysis pipeline:
1. Extract facts from this document
2. Map facts to patterns
3. Generate the three output summaries

Then provide the three outputs:
- attorney-summary.md
- gal-clinician-summary.md
- internal-clarity.md

Format each output clearly with a header like "=== attorney-summary.md ===" followed by the complete content."""

    try:
        # Call Claude API
        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=16000,
            system=system_context,
            messages=[{
                "role": "user",
                "content": user_message
            }]
        )

        # Extract the response text
        response_text = response.content[0].text

        # Parse the three outputs from the response
        outputs = parse_claude_outputs(response_text)

        # Save outputs to files
        for output_name, content in outputs.items():
            filepath = OUTPUT_FOLDER / output_name
            filepath.write_text(content, encoding='utf-8')

        return outputs

    except Exception as e:
        raise Exception(f"Claude API error: {str(e)}")


def parse_claude_outputs(response_text):
    """
    Parse Claude's response to extract the three output files.
    Looks for markers like "=== attorney-summary.md ===" to split content.
    """
    outputs = {
        'attorney-summary.md': '',
        'gal-clinician-summary.md': '',
        'internal-clarity.md': ''
    }

    # Try to find sections marked with === filename ===
    current_output = None
    current_content = []

    for line in response_text.split('\n'):
        # Check for output markers
        if '===' in line and 'attorney-summary' in line.lower():
            if current_output and current_content:
                outputs[current_output] = '\n'.join(current_content).strip()
            current_output = 'attorney-summary.md'
            current_content = []
        elif '===' in line and ('gal' in line.lower() or 'clinician' in line.lower()):
            if current_output and current_content:
                outputs[current_output] = '\n'.join(current_content).strip()
            current_output = 'gal-clinician-summary.md'
            current_content = []
        elif '===' in line and 'internal' in line.lower():
            if current_output and current_content:
                outputs[current_output] = '\n'.join(current_content).strip()
            current_output = 'internal-clarity.md'
            current_content = []
        elif current_output:
            # Don't include the === marker line itself
            if '===' not in line:
                current_content.append(line)

    # Save the last section
    if current_output and current_content:
        outputs[current_output] = '\n'.join(current_content).strip()

    # If parsing failed, try to salvage what we can
    if not any(outputs.values()):
        # Fallback: just put the whole response in internal-clarity
        outputs['internal-clarity.md'] = response_text
        outputs['attorney-summary.md'] = "Output parsing failed. See internal-clarity.md for full response."
        outputs['gal-clinician-summary.md'] = "Output parsing failed. See internal-clarity.md for full response."

    return outputs


def read_output_file(filename):
    """Read content from an output file."""
    filepath = OUTPUT_FOLDER / filename
    if filepath.exists():
        return filepath.read_text(encoding='utf-8')
    return None


@app.route('/')
def index():
    """Serve the main page."""
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    """Handle file upload and trigger Claude API analysis."""

    # Check if file was included
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400

    file = request.files['file']

    # Check if filename is empty
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    # Validate file type
    if not allowed_file(file.filename):
        return jsonify({
            'error': 'Invalid file type. Please upload a .txt or .md file.'
        }), 400

    # Read file content directly (no need to save to disk)
    try:
        file_content = file.read().decode('utf-8')
    except Exception as e:
        return jsonify({
            'error': f'Unable to read file: {str(e)}'
        }), 400

    # Get the original filename
    filename = secure_filename(file.filename)

    try:
        # Analyze document using Claude API with Kiro context
        outputs = analyze_document_with_claude(file_content, filename)

        # Return success with outputs
        return jsonify({
            'success': True,
            'outputs': {
                'attorney': outputs.get('attorney-summary.md', 'No attorney summary generated.'),
                'gal': outputs.get('gal-clinician-summary.md', 'No GAL/clinician summary generated.'),
                'internal': outputs.get('internal-clarity.md', 'No internal clarity document generated.')
            }
        })

    except Exception as e:
        return jsonify({
            'error': f'Analysis failed: {str(e)}'
        }), 500


@app.route('/download/<filename>')
def download_file(filename):
    """Serve output files for download."""
    
    # Whitelist allowed filenames
    allowed_files = {
        'attorney-summary.md',
        'gal-clinician-summary.md',
        'internal-clarity.md'
    }
    
    if filename not in allowed_files:
        return jsonify({'error': 'File not found'}), 404
    
    filepath = OUTPUT_FOLDER / filename
    
    if not filepath.exists():
        return jsonify({'error': 'File not found'}), 404
    
    return send_file(
        filepath,
        as_attachment=True,
        download_name=filename
    )


@app.errorhandler(413)
def too_large(e):
    """Handle file too large error."""
    return jsonify({
        'error': 'File too large. Please upload a file under 5MB (~10 pages).'
    }), 413


if __name__ == '__main__':
    print("\n" + "="*60)
    print("  North Star for High-Conflict Cases")
    print("  Local Analysis Tool")
    print("="*60)
    print("\n  Open your browser to: http://localhost:5000")
    print("\n  Press Ctrl+C to stop the server")
    print("="*60 + "\n")
    
    app.run(debug=False, host='127.0.0.1', port=5000)
