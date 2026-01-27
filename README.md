# North Star for High-Conflict Cases

**A pattern-mapping tool for high-conflict custody documentation**

Built for the Dynamous & Kiro CLI Hackathon (January 2025)

---

## What It Does

North Star analyzes custody documentation and maps evidence to 10 research-backed child-impact patterns. It generates three audience-specific outputs:

| Output | Audience | Focus |
|--------|----------|-------|
| **Attorney Summary** | Legal counsel | Facts only, patterns meeting threshold |
| **GAL/Clinician Summary** | Guardian ad Litem, therapists | Child-impact framing |
| **Internal Clarity** | Documenting parent | Full transparency, ALL patterns |

**Key principle:** The AI maps to predefined patterns. It does not discover, diagnose, or conclude. All facts are extracted verbatim from source documents.

---

## Two Ways to Run It

### Path 1: Kiro CLI (for judges/developers)

```bash
# Open terminal and navigate to project
cd ~/Desktop/north-star-high-conflict

# Start Kiro CLI
kiro-cli

# Run the analysis prompt
@analyze

# When prompted, provide the document path:
/Users/[your-username]/Desktop/north-star-high-conflict/sample-docs/case-001.md
```

Outputs are written to `/outputs/`.

### Path 2: Flask Web UI (for end users)

```bash
# Set your Anthropic API key (one time)
export ANTHROPIC_API_KEY=your-key-here

# Start the Flask server
python3 ui/app.py

# Open browser to:
# http://127.0.0.1:5000
```

Upload a document, click "Analyze Documentation", view results in browser.

---

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                 SHARED INTELLIGENCE                          │
│  .kiro/steering/ + .kiro/prompts/ + reference/              │
└─────────────────────────────────────────────────────────────┘
              │                              │
              ▼                              ▼
┌─────────────────────────┐    ┌─────────────────────────────┐
│     KIRO CLI PATH       │    │      FLASK WEB UI PATH      │
│  (judges/developers)    │    │      (end users/parents)    │
│                         │    │                             │
│  Human runs @analyze    │    │  Flask calls Claude API     │
│  in Kiro IDE            │    │  with same prompts          │
└─────────────────────────┘    └─────────────────────────────┘
```

**Why two paths?** Kiro CLI has no headless mode. Flask loads the same steering docs + prompts and calls the Claude API directly. Same intelligence, different interfaces.

---

## The 10 Child-Impact Patterns

| Category | Pattern | Threshold |
|----------|---------|-----------|
| Critical | Medical/Therapeutic Interference | 2+ incidents |
| Serious | Boundary Violations | 3+ incidents |
| Serious | Coaching/Secrecy Behaviors | 3+ incidents |
| Serious | Distorted Narratives | 3+ incidents |
| Behavioral | Negative Parent Portrayal | 5+ incidents |
| Behavioral | Triangulation/Messenger Role | 5+ incidents |
| Behavioral | Parentification | 5+ incidents |
| Logistical | Co-Parent Communication Breakdown | 5+ incidents |
| Logistical | Financial Impact Patterns | 5+ incidents |
| Logistical | Schedule & Transition Disruption | 5+ incidents |

Patterns are derived from peer-reviewed research on high-conflict custody and parental alienation. See `reference/child-impact-patterns.md` for full taxonomy with citations.

---

## Project Structure

```
north-star-high-conflict/
├── .kiro/
│   ├── steering/           # Product, tech, structure docs
│   ├── prompts/            # Kiro prompts (analyze, extract, map, generate)
│   └── agents/             # Analyst agent configuration
├── reference/
│   └── child-impact-patterns.md   # 10-pattern taxonomy
├── ui/
│   ├── app.py              # Flask application
│   ├── templates/          # HTML templates
│   └── static/             # CSS styles
├── sample-docs/
│   ├── case-001.md         # 12 incidents (Medical, Communication)
│   ├── case-002.md         # 28 incidents (Boundary, Coaching, Triangulation)
│   └── case-003.md         # 42 incidents (Financial, Parentification, Distorted)
├── outputs/                # Generated analysis files
├── docs/
│   └── DEVLOG.md           # Development log (for judges)
├── requirements.txt        # Python dependencies
└── README.md               # This file
```

---

## Setup

### Prerequisites
- Python 3.8+
- Anthropic API key (for Flask path) — Free at [console.anthropic.com](https://console.anthropic.com) (new accounts get $5 free credits)
- Kiro CLI installed (for Kiro path)

> **Note for Judges:** The Flask Web UI requires an Anthropic API key. New Anthropic accounts receive $5 in free credits — more than enough to test the application. Alternatively, you can test the Kiro CLI path which uses your existing Kiro/Claude setup.

### Installation

```bash
# Clone the repository
git clone https://github.com/ashleycmk/north-star-high-conflict.git
cd north-star-high-conflict

# Install dependencies
pip3 install -r requirements.txt

# Set API key (for Flask path)
cp .env.example .env
# Edit .env and add your ANTHROPIC_API_KEY
```

---

## Sample Documents

Three test documents demonstrate different pattern profiles:

| Document | Timespan | Incidents | Primary Patterns |
|----------|----------|-----------|------------------|
| `case-001.md` | 10 months | 12 | Medical Interference, Communication Breakdown |
| `case-002.md` | 2 years | 28 | Boundary Violations, Coaching/Secrecy, Triangulation |
| `case-003.md` | 2 years | 42 | Financial Impact, Parentification, Distorted Narratives |

Each document surfaces different patterns, demonstrating the system's ability to identify varied child-impact concerns from documentation.

See `/outputs/` for example outputs.

---

## Safety Constraints

- **Pattern mapping, not discovery**: AI matches to predefined categories only
- **No diagnosis**: Never labels individuals or suggests clinical conditions
- **No legal advice**: Outputs are orientation tools, not legal documents
- **Evidence locking**: All facts preserved verbatim; gaps marked `[UNCLEAR]`
- **Privacy**: All processing is local; no data leaves your machine

---

## Development Log

See [docs/DEVLOG.md](docs/DEVLOG.md) for the complete build journey, including:
- Day-by-day progress
- Key decisions and rationale
- Technical challenges and solutions
- Time investment (~56+ hours)

---

## Built With

- **Kiro CLI** - Agentic development environment
- **Claude API** - AI analysis via Anthropic
- **Flask** - Web framework for UI path
- **Python** - Backend logic

---

## Kiro CLI Features Used

This project leverages Kiro CLI extensively:

### Steering Documents
- `product.md` — Product vision, user journey, success criteria
- `tech.md` — Technical architecture, pattern mapping design, safety constraints
- `structure.md` — File structure, output formats, naming conventions

### Custom Prompts (4 project-specific)
| Prompt | Purpose |
|--------|---------|
| `@analyze` | Main orchestrator — runs full 3-step analysis pipeline |
| `extract-facts.md` | Step 1 — separates facts from emotional language |
| `map-patterns.md` | Step 2 — maps facts to 10 predefined patterns |
| `generate-outputs.md` | Step 3 — creates 3 audience-specific outputs |

### Agent Configuration
- `analyst-agent.json` — Non-authoritative analysis agent with strict positioning constraints

### Template Prompts Used
- `@prime` — Load project context
- `@code-review-hackathon` — Evaluate against judging criteria

### What Makes This a "Kiro Project"
The intelligence lives in `.kiro/`. All analysis logic resides in steering docs and prompts, not hardcoded. The Flask Web UI loads the same Kiro prompts as system context, ensuring both paths deliver identical analysis quality.

---

## Author

Built by Ashley for the Dynamous & Kiro CLI Hackathon

*"You know something is wrong. You just don't know what to call it."*

---

## License

This project is submitted for the Dynamous & Kiro CLI Hackathon (January 2025).
