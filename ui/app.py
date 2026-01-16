"""
North Star for High-Conflict Cases
Flask Web Application

A local-only web interface for the North Star CLI analysis tool.
Runs at localhost:5000 - no internet connection required.
"""

import os
import subprocess
from pathlib import Path
from flask import Flask, render_template, request, jsonify, send_file
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Configuration
BASE_DIR = Path(__file__).resolve().parent.parent
UPLOAD_FOLDER = BASE_DIR / 'uploads'
OUTPUT_FOLDER = BASE_DIR / 'outputs'
ALLOWED_EXTENSIONS = {'txt', 'md'}
MAX_CONTENT_LENGTH = 5 * 1024 * 1024  # 5MB max (~10 pages)

# Ensure directories exist
UPLOAD_FOLDER.mkdir(exist_ok=True)
OUTPUT_FOLDER.mkdir(exist_ok=True)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = MAX_CONTENT_LENGTH


def allowed_file(filename):
    """Check if file extension is allowed."""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


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
    """Handle file upload and trigger Kiro analysis."""
    
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
    
    # Save the file
    filename = secure_filename(file.filename)
    filepath = UPLOAD_FOLDER / filename
    file.save(filepath)
    
    try:
        # Run Kiro analysis
        # The command: kiro run analyze --input <filepath>
        result = subprocess.run(
            ['kiro', 'run', 'analyze', '--input', str(filepath)],
            capture_output=True,
            text=True,
            timeout=120,  # 2 minute timeout
            cwd=BASE_DIR
        )
        
        # Check if analysis succeeded
        if result.returncode != 0:
            # Clean up uploaded file
            filepath.unlink(missing_ok=True)
            return jsonify({
                'error': 'Analysis failed. Please check your file format.',
                'details': result.stderr
            }), 500
        
        # Read the generated outputs
        attorney = read_output_file('attorney-summary.md')
        gal = read_output_file('gal-clinician-summary.md')
        internal = read_output_file('internal-clarity.md')
        
        # Clean up uploaded file
        filepath.unlink(missing_ok=True)
        
        # Return success with outputs
        return jsonify({
            'success': True,
            'outputs': {
                'attorney': attorney or 'No attorney summary generated.',
                'gal': gal or 'No GAL/clinician summary generated.',
                'internal': internal or 'No internal clarity document generated.'
            }
        })
        
    except subprocess.TimeoutExpired:
        filepath.unlink(missing_ok=True)
        return jsonify({
            'error': 'Analysis timed out. Please try a smaller file.'
        }), 500
    except FileNotFoundError:
        filepath.unlink(missing_ok=True)
        return jsonify({
            'error': 'Kiro CLI not found. Please ensure Kiro is installed.'
        }), 500
    except Exception as e:
        filepath.unlink(missing_ok=True)
        return jsonify({
            'error': f'An unexpected error occurred: {str(e)}'
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
