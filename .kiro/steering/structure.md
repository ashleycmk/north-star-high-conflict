# Project Structure

# Project Structure

## Directory Layout

```
north-star-high-conflict/
├── .kiro/
│   ├── steering/                    # Persistent project constraints and principles
│   │   ├── product.md               # Product purpose, boundaries, success criteria
│   │   ├── tech.md                  # Technical architecture and safety constraints
│   │   └── structure.md             # This file: directory layout and conventions
│   ├── prompts/                     # Spec-driven workflow prompts
│   │   ├── analyze.md               # Main analysis entry point
│   │   ├── extract-facts.md         # Fact extraction and emotion separation
│   │   ├── map-patterns.md          # Pattern mapping to taxonomy
│   │   └── generate-outputs.md      # Output generation for all audiences
│   ├── agents/                      # Custom agent definitions
│   │   └── analyst-agent.json       # Single analysis agent definition
│   └── settings/                    # Kiro configuration
├── reference/
│   └── child-impact-patterns.md     # Static pattern taxonomy (non-authoritative)
├── ui/
│   ├── app.py                       # Flask application (minimal web server)
│   ├── templates/
│   │   └── index.html               # Single-page upload interface
│   └── static/
│       └── style.css                # Minimal styling
├── outputs/                         # Generated artifacts (runtime only)
│   ├── attorney-summary.md          # Facts only, neutral, ranked
│   ├── gal-clinician-summary.md     # Child-impact framing, factual
│   └── internal-clarity.md          # Prioritization transparency
├── docs/
│   └── DEVLOG.md                    # Development log (judging + traceability)
├── examples/
│   └── sample-input.md              # Example input document for testing/demo
├── README.md                        # Setup, usage, and boundaries (root level)
├── requirements.txt                 # Python dependencies (Flask)
└── run.sh                           # Single entry command to start application
```

## UI Scope and Constraints

The `ui/` directory contains a minimal Flask application that serves as a local web wrapper for the CLI.

**What the UI does:**
- Provides a single-page upload interface
- Displays a progress indicator during processing
- Shows generated outputs for viewing/download
- Runs locally at `localhost` (no internet hosting)

**What the UI does NOT do:**
- Contains no analysis, prioritization, or decision logic
- Does not modify, filter, or interpret outputs
- Does not store documents or results beyond the current session

**All core behavior is implemented in Kiro prompts.** The UI exists solely to make the tool accessible to non-technical users and to improve demo clarity for judges.

## File Naming Conventions

- Lowercase, hyphenated filenames (e.g., `extract-facts.md`, `child-impact-patterns.md`)
- Descriptive, explicit names that convey purpose
- No abbreviations unless universally understood
- No full personal names in any filenames

## Identity Referencing Rules

All generated outputs follow strict identity protection:

- Individuals are referenced using **role-based identifiers with optional first-name initials**
  - `P1 (A.)` — Parent 1 (initial A.)
  - `P2 (J.)` — Parent 2 (initial J.)
  - `C1 (C.)` — Child 1 (initial C.)
  - `W1 (B.)` — Witness 1 (initial B.)
- Full personal names are **never generated or inferred**
- Identity mappings appear **only** in the internal clarity output
- Professional-facing summaries contain **no identity mappings**
- The uploaded document is the **sole source** for any role or initial assignment

## Module Organization

The system follows a **linear, single-responsibility pipeline**:

```
Input Document
     ↓
┌─────────────────────────┐
│  1. Ingestion           │  Parse and validate input
└─────────────────────────┘
     ↓
┌─────────────────────────┐
│  2. Fact Extraction     │  Separate facts from emotion/interpretation
└─────────────────────────┘
     ↓
┌─────────────────────────┐
│  3. Pattern Mapping     │  Map facts to predefined taxonomy
└─────────────────────────┘
     ↓
┌─────────────────────────┐
│  4. Relevance Weighting │  Score across professional lenses
└─────────────────────────┘
     ↓
┌─────────────────────────┐
│  5. Output Rendering    │  Generate audience-specific summaries
└─────────────────────────┘
     ↓
Three Output Files
```

**Pipeline principles:**
- No shared mutable state between stages
- Each stage has a single responsibility
- Outputs from one stage are inputs to the next
- All stages are auditable and deterministic

## Configuration Files

### `.kiro/steering/`
Defines all non-negotiable system constraints:
- Product purpose and boundaries
- Technical architecture and safety controls
- Structural conventions and identity rules

Steering files are **always loaded** by Kiro and provide persistent context across all conversations.

### `.kiro/prompts/`
Encodes spec-driven workflow prompts:
- Each prompt handles one pipeline stage
- Prompts reference steering docs for constraints
- Prompts reference pattern taxonomy for mapping

### `.kiro/agents/`
Contains the single agent definition:
- Tool permissions (read-only for analysis)
- Resource access (steering docs, pattern taxonomy)
- Behavioral constraints (no advice, no diagnosis)

### `.kiro/settings/`
Local Kiro configuration only. No secrets, tokens, or environment variables required.

## Output Files

All generated outputs are written to `/outputs/`:

| File | Audience | Content |
|------|----------|---------|
| `attorney-summary.md` | Legal counsel | Facts only, neutral language, ranked by relevance |
| `gal-clinician-summary.md` | GALs, therapists | Child-impact framing, behavioral patterns, factual |
| `internal-clarity.md` | Parent (private) | Why examples were prioritized, pattern rationale |

**Output rules:**
- Outputs are **overwritten** on each run
- Outputs are treated as **read-only** by the system
- Outputs contain **explicit disclaimers** about limitations

## Documentation Structure

### `README.md` (root level)
- What the tool does (one paragraph)
- What it explicitly does NOT do (disclaimers)
- Prerequisites and setup instructions
- How to run it (under 2 minutes)
- Project structure overview

### `docs/DEVLOG.md`
- Daily development notes with timestamps
- Design decisions and rationale
- Scope cuts and trade-offs logged explicitly
- Maintained throughout development for judging transparency

## Reference Files

### `reference/child-impact-patterns.md`
- Static pattern taxonomy (not generated at runtime)
- Non-authoritative: derived from published frameworks
- Used for **mapping**, not discovery
- Never modified by the system

## Asset Organization

- Minimal local UI assets only
- No external stylesheets, CDNs, or media assets
- Single CSS file for basic styling
- No JavaScript frameworks

## Build Artifacts

- All generated outputs are written to `/outputs/`
- Outputs are overwritten per run
- Outputs are treated as read-only by the system

## Environment Constraints

- **Local execution only** — no cloud services, external APIs, or hosting
- **No staging/production environments** — single local environment
- **No environment-specific branching** — same behavior everywhere
- **No secrets or tokens** — nothing to configure

These constraints are intentional to ensure:
- Reproducibility across machines
- Privacy of sensitive documents
- Auditability of all processing
- Simplicity for hackathon judging