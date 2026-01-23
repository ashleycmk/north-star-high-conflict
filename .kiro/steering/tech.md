# Technical Architecture

## Technology Stack
- **Kiro CLI** — core execution, orchestration, and prompt workflow
- **LLM via Kiro runtime** — single-model inference with strict constraints
- **Local Web UI** — thin, local-only interface for non-technical users
- **Local file system** — temporary input handling and output generation
- **Markdown / plain text** — all artifacts are human-readable and auditable

MVP intentionally avoids external APIs, databases, cloud services, accounts, or networking.

## Architecture Overview

North Star for High-Conflict Cases is a **CLI-first analysis engine with a thin local UI wrapper**.

### Core Layers

1. **Core Analysis Engine (CLI)**
   - Accepts a single text or markdown document
   - Executes a fixed, linear, spec-driven pipeline:
     - Fact extraction and emotion suppression
     - Intra-document pattern detection
     - Pattern prioritization using perspective-based relevance rubrics (attorney, GAL, clinician)
   - Enforces a **pattern-first output model**:
     - Up to **3 patterns**
     - Up to **3 supporting instances per pattern**
   - Generates structured, read-only outputs

2. **Local User Interface (UI)**
   - Runs as a local web application
   - Allows file upload and one-click execution
   - Invokes the same Kiro CLI command
   - Displays and enables download of outputs
   - Contains **no analysis or decision logic**

All business logic and constraints live in the CLI layer.

## Pattern Mapping Architecture (Critical)

**The system MAPS facts to predefined patterns. It does NOT discover or invent patterns.**

This is a fundamental architectural decision that affects safety, defensibility, and output quality.

### How Pattern Mapping Works

1. **Extract** — Pull factual statements from the uploaded document
2. **Compare** — Match facts against the predefined pattern taxonomy (`reference/child-impact-patterns.md`)
3. **Group** — Cluster repeated, fact-supported instances under matching categories
4. **Threshold** — Surface patterns only when multiple instances support them

### What the System Does NOT Do

- Does not invent new pattern categories
- Does not infer patterns from single incidents
- Does not label behavior beyond taxonomy definitions
- Does not draw diagnostic or legal conclusions
- Does not fill gaps with assumptions

### Why This Matters

| Approach | Risk | Our Choice |
|----------|------|------------|
| Pattern Discovery | AI invents labels, hallucinates connections | ❌ Rejected |
| Pattern Mapping | AI matches facts to established frameworks | ✅ Chosen |

Pattern mapping is safer because:
- Patterns are predefined and reviewable
- No AI-generated labels or interpretations
- Outputs are traceable to source taxonomy
- Professional judgment remains with humans

The pattern taxonomy is derived from published forensic psychology literature and family court evaluation frameworks. It is descriptive, not diagnostic.

## Development Environment

- Kiro CLI installed locally
- Local execution only (no secrets, tokens, or environment variables)
- Project runs via a single command
- UI and CLI run on the same machine

Setup requires cloning the repository and running the provided startup command.

## Code Standards

- Explicit, readable naming; no abstraction for abstraction's sake
- Linear, inspectable control flow
- Deterministic structure for identical inputs
- No hidden state or adaptive learning
- **Evidence-locking rules**:
  - Missing dates marked as `Date: NONE`
  - Unclear attribution marked as `[UNCLEAR]`
  - Gaps are flagged, never filled
- **Pattern threshold enforcement**:
  - A pattern must be supported by at least two documented incidents
- **Language risk suppression**:
  - No diagnosis, intent attribution, or legal conclusions
  - Observable behavior and direct quotes only

Auditability is prioritized over cleverness.

## Testing Strategy

- Manual, example-driven testing using representative documents
- Verification that:
  - The CLI runs end-to-end without failure
  - Outputs are generated consistently
  - Pattern limits (max 3 patterns / 3 instances) are enforced
  - Professional-facing outputs remain factual and restrained
- Automated testing is intentionally excluded from MVP to maintain scope discipline

## Deployment Process

There is no production deployment.

The tool is distributed as a local application:
- Users or judges run it on their own machines
- No hosting, build pipeline, or external infrastructure required

## Performance Requirements

- Single-document processing only
- Typical execution completes within seconds
- No concurrency or scalability requirements in MVP

Performance is sufficient if execution is reliable and predictable.

## Security Considerations

- All processing occurs locally
- No data transmission or external storage
- No authentication or user accounts
- Input documents are processed only for the duration of execution
- Outputs are written only to user-controlled local directories

### Safety and Hallucination Controls

- **Source isolation**: outputs may only reference the uploaded document
- **No gap-filling**: missing or ambiguous information is flagged, not inferred
- **Audit trail**: surfaced instances include direct quotes or references where available
- **Hard boundaries**:
  - No legal advice or filing strategy
  - No medical or psychological diagnosis
  - No claims of professional authority

Risk is minimized by eliminating persistence, networking, and external dependencies.

## Optional Static Knowledge Reference (Non-Authoritative)

A small, local **Pattern Definitions Pack** may be included as static markdown:
- Neutral definitions of patterns
- What qualifies as evidence vs. non-evidence
- No research claims, statistics, or authority assertions

This reference supports consistency but never introduces facts about the user's case.