# North Star — Development Log
## Hackathon Documentation

**Project:** North Star for High-Conflict Cases
**Hackathon:** Dynamous & Kiro CLI ($17K prize pool)
**Deadline:** ~~January 23, 2025~~ **January 30, 2025, 11:59 PM PST** (extended)
**Winners Announced:** February 14, 2025
**Start Date:** January 12, 2025

---

## Day 1 — Monday, January 12 (~4 hours)

### Focus: Research & Foundation

#### What I Did
- Set up Claude project with hackathon context
- Established working relationship dynamic: "Claude leads, I execute"
- Created initial project strategy and 8-day implementation plan

#### Key Decisions
- CLI-first architecture (not web-first)
- Local execution only (privacy requirement)
- Pattern mapping, not pattern discovery
- Non-authoritative positioning: "Orientation, not authority"

#### Strategic Foundation
- Identified 40 judging points for Application Quality
- Identified 20 points for Kiro CLI usage
- Identified 20 points for Documentation (DEVLOG critical)

---

## Day 2 — Tuesday, January 13 (~6 hours)

### Focus: Architecture & Specification

#### What I Did
- Defined complete product specification
- Established three-output model:
  1. attorney-summary.md (facts only, top 3 patterns)
  2. gal-clinician-summary.md (child-impact framing, top 3 patterns)
  3. internal-clarity.md (full transparency, ALL patterns)
- Created steering document framework

#### Key Decisions
- Flask UI → Kiro CLI → Outputs architecture
- Single document analysis only (MVP constraint)
- Evidence locking: verbatim preserved, gaps marked `[UNCLEAR]`
- Identity format: P1 (A.), P2 (J.), C1 (C.)

---

## Day 3 — Wednesday, January 14 (~7 hours)

### Focus: Tool Migration & Steering Documents

#### Morning Session (7:00 AM – 11:45 AM)
- Continued strategy refinement
- Reviewed implementation status against plan
- **Critical realization:** ChatGPT effective for strategy but hitting limits for implementation

#### Migration Decision
Made decision to migrate from ChatGPT to Claude for execution phase:
- Claude's file creation capabilities better suited for building
- Need to generate real files, not just discuss them
- Strategy complete; execution is the bottleneck

**The Real Reason:** ChatGPT fabricated information. With confidence. The kind of confidence that makes you doubt yourself before you doubt it.

I caught it. Fired it.

But here's what people miss: **I still had to babysit the one I kept.**

Direct quotes from me pushing back on Claude throughout this build:
- "SLOW DOWN. You're sure this is everything?"
- "That is UNACCEPTABLE. You should NEVER make anything up."
- "This isn't as long as the first version you gave me..." (Caught Claude cutting 400 lines. FOUR HUNDRED.)
- "Good lord. Remember YOU are the expert here and you need to be leading this process effectively."

**The lesson:** I fired one AI assistant. And I still have to parent the one I kept.

#### Afternoon Session (2:00 PM – 4:00 PM)
Committed to GitHub:
- [x] DEVLOG.md created
- [x] structure.md — corrected and committed
- [x] tech.md — added Pattern Mapping Architecture section
- [x] README.md — drafted

#### Key Decision
child-impact-patterns.md must be built from actual research/reports, NOT AI-drafted guesses. Separate working session needed.

---

## Day 4 — Thursday, January 15 (~10 hours)

### Focus: Pattern Taxonomy & First Prompt

#### Morning Session (10:00 AM – 12:00 PM)
- Compiled 9 research reports from Google Drive (IL family law, parental alienation, communication strategies)
- Created comprehensive briefing document for pattern extraction
- Discovered structural issue: "Safety & Environmental Concerns" didn't fit behavioral focus

#### Pattern Taxonomy Breakthrough
Reframed "Safety Concerns" → "Boundary Violations" (information-based boundary collapse)
- All 10 patterns now describe observable parent behaviors
- Each pattern has 11 required sections from research

#### Afternoon Session
Completed and committed:
- [x] child-impact-patterns.md (658 lines, 10 research-backed patterns)
- [x] extract-facts.md — drafted, audited, LOCKED
- [x] README.md committed to repo root

#### LinkedIn "Build in Public" Launched
**Day 1 Post:** "Stress-test optimism" — the absurd math of starting 10 days late, shooting for top 10

#### Key Decisions
- Pattern mapping NOT discovery (safety constraint)
- Map ALL patterns that meet threshold → narrow to top 3 for professional outputs
- 6-tag fact extraction system: MEDICAL | COMMUNICATION | SCHEDULE | FINANCIAL | CHILD-BEHAVIOR | BOUNDARY

---

## Day 5 — Friday, January 16 (~8 hours)

### Focus: UI Completion, Prompt Finalization, Flask Conversion

#### Morning Session (9:00 AM – 11:30 AM)

**UI DESIGN COMPLETE — MVP LOCKED:**
- [x] Full UI/UX design with 5 states (Homepage, File Selected, Processing, Results, Error)
- [x] Major positioning breakthrough: **parents need translation, not organization**
- [x] 10 research-backed patterns with gut-punch quote descriptions
- [x] Three audience-specific outputs with educational context
- [x] "Why I Built This" origin story
- [x] Professional design system (purple #5B3D8C)
- [x] Key deliverable: `north-star-final.jsx` — LOCKED

**LinkedIn Day 2 Posted:**
- AI "Org Chart" (Claude, Perplexity, Kiro, ChatGPT-fired)
- Educational nugget: Foundation first, UI last

#### Afternoon Session

**Prompt Development:**
- [x] map-patterns.md — audited and LOCKED
- [x] Implemented tiered threshold system:
  - Critical (2+): Medical/Therapeutic Interference
  - Serious (3+): Boundary Violations, Coaching/Secrecy, Distorted Narratives
  - Behavioral (5+): Negative Parent Portrayal, Triangulation, Parentification
  - Logistical (5+): Communication Breakdown, Financial Impact, Schedule Disruption
- [x] generate-outputs.md — drafted and approved

**React → Flask Conversion:**
- [x] Converted entire React component to Flask/HTML/CSS
- [x] Created app.py, index.html, style.css, requirements.txt
- [x] All files committed to GitHub ui/ folder
- [x] Learned folder structure creation via GitHub web interface

#### The Positioning Breakthrough

The insight came while explaining the problem to Claude:

> "An attorney says 'give me 10 examples.' A parent has years of notes. How do they know what to pull?"

The answer unlocked everything:

**Parents don't need better organization tools — they need TRANSLATION tools. They need the VOCABULARY.**

The headline that captures it: *"You know something is wrong. You just don't know what to call it."*

#### Key Insight
The positioning breakthrough ("vocabulary, not organization") crystallized the entire product message: parents don't need better organization tools — they need **translation tools** that help them understand what their documentation reveals.

---

## Day 6 — Saturday, January 17 (~1 hour)

### Focus: Strategic Rest Day

#### What Happened
- Deliberate break to avoid burnout before final push
- Drafted LinkedIn "push back on AI" educational post
- Saved educational content for Monday (better weekday engagement)

#### Key Decision
Strategic rest — sustainable pace for final stretch.

---

## Day 7 — Sunday, January 18 (~1 hour)

### Focus: Personal Day + Light LinkedIn

#### What Happened
- Dad's 77th birthday celebration at wndr museum
- Posted LinkedIn Day 3 about the personal milestone

#### Key Insight
Building in public means sharing the human side too, not just the grind.

---

## Day 8 — Monday, January 19 (~1 hour)

### Focus: Light Day + LinkedIn

#### What Happened
- Posted LinkedIn Day 4 (Karpathy repost about feeling behind on AI/programming)
- Added personal reflection connecting to hackathon journey

#### Major News
**Hackathon deadline extended from January 23 to January 30!** Winners announced February 14.

This changes everything — 10 extra days to polish.

---

## Day 9 — Tuesday, January 20 (~6 hours)

### Focus: Resume Build & Blocker Discovery

#### DEVLOG Catch-up
- Updated DEVLOG with Days 4-8 entries
- Verified GitHub repo state

#### Build Work
- [x] generate-outputs.md committed to GitHub
- [x] Started analyze.md (main orchestrator prompt)

#### CRITICAL BLOCKER DISCOVERED
**Kiro has no headless mode.**

Tested extensively:
| Command | Result |
|---------|--------|
| `kiro chat --headless` | ❌ "not in the list of known options" |
| `kiro --batch` | ❌ "not in the list of known options" |
| `kiro serve-web` | ❌ requires kiro-tunnel (not available) |

**Implication:** Flask cannot programmatically call Kiro via subprocess. The original UI integration approach won't work.

#### Key Decision
The product IS the Kiro project itself. Judges clone repo → open in Kiro → run analysis in Kiro's chat.

---

## Day 10 — Wednesday, January 21 (~5 hours)

### Focus: analyze.md Completion & Integration Troubleshooting

#### analyze.md COMPLETE
- Created main orchestrator prompt
- Sent to second Claude thread for audit
- Issues identified: missing "Why This Format?" sections, fact type inconsistencies, emerging pattern references
- All fixes applied
- **analyze.md committed to GitHub**

#### GitHub Verification
All 4 Kiro prompts now in `.kiro/prompts/`:
- analyze.md (10,892 bytes)
- extract-facts.md (10,795 bytes)
- map-patterns.md (15,785 bytes)
- generate-outputs.md (12,773 bytes)

#### Kiro Integration Troubleshooting
- Discovered Kiro was looking at wrong folder
- Fix: `cd ~/Downloads/north-star-high-conflict && kiro .`
- Posted in hackathon community Discord asking for help
- Consulted with developer friend Justin

#### Status Check
All architecture complete. Blocked on: Kiro integration.

---

## Day 11 — Thursday, January 22 (~3 hours)

### Focus: LinkedIn Day 5 & Tyler Call

#### LinkedIn Day 5 Posted
"The Struggle Bus Has No Brakes"
- Claude unavailability issues
- Deadpan chaos: Claude is my developer, PM, therapist, entire engineering team
- "The delusion is load-bearing at this point"

#### Tyler Call (12:37 PM)

Developer friend Tyler got on the phone.

**Tyler:** "Are you using Claude Code?"
**Me:** "I'm not using Claude Code at all."
**Tyler:** "Do you have VS Code?"
**Me:** "I do not."
**Tyler:** "You'll eventually want to."

I laughed out loud. Not a panic laugh. A "well, I guess we're doing this now" laugh.

**Tyler's insight:** "You've been asking Claude to HELP you code. Stop. Use Claude Code to BUILD with an agent that has all your project context."

**Translation:**
- Claude = asking a smart friend for advice
- Claude Code = hiring a specialist who read your entire project file first

**Tyler's warning:** "Might be something where you literally just need to change one line and you'll be like, motherfucker."

#### Decision
Abandon direct Kiro integration struggles. Pivot to Claude Code + VS Code.

---

## Day 12 — Friday, January 23 (~4.5 hours + evening session TBD)

### Focus: The Pivot — From Lost to Breakthrough

**Started:** ~9:00 AM
**Break:** 1:30 PM for calls, gym, reset

**Context:** After 3+ days stuck on Kiro headless limitation, feeling completely lost. No working product. Deadline in 7 days.

#### Morning Session (9:00 AM – 1:30 PM)

**The Decision:**
Made the call to pivot from 1 system I don't understand (Kiro subprocess integration) to 3 systems I have ZERO experience with:
1. **Claude Code** (never used it)
2. **VS Code** (never used it)
3. **Anthropic API** (never set one up)

**Why this was terrifying:**
- I'm not a developer
- Adding complexity when already blocked feels insane
- 7 days to deadline
- But fuck it — go big or go home

**Setup Process:**
- Created handoff documents for Claude Code
- Installed VS Code (first time opening it)
- Installed Claude Code extension
- Set up Anthropic API account at console.anthropic.com
- Created API key: `north-star-hackathon`
- Configured .env file (learned what environment variables are)

**The UI Realization (CRITICAL):**
Claude Code initially proposed dropping the web UI entirely. Pure Kiro CLI only.

**I pushed back hard.**

Why? Because the UI isn't a delivery mechanism — it's THE WHOLE POINT:
- The emotional validation ("You know something is wrong. You just don't know what to call it")
- The stats showing parents they're not alone
- The education about WHY professionals need different language
- The 10 patterns with gut-punch quotes that make parents feel SEEN
- The origin story that says "I built this because I was you"

**This is not about file uploads and buttons. This is about a parent in crisis feeling validated for the first time.**

Claude Code got it. Immediately proposed dual-path architecture:
- **Path 1:** Pure Kiro CLI for judges/developers
- **Path 2:** Web UI with Claude API for real parents

This turns the Kiro limitation into INNOVATION: we built for two completely different audiences with the same underlying intelligence.

#### Afternoon Session (12:00 PM – 3:30 PM)

**Infrastructure Setup:**
- [x] Created .gitignore (protects .env from GitHub)
- [x] Created requirements.txt (Flask, anthropic, python-dotenv, markdown)
- [x] Installed all Python dependencies via pip3
- [x] Created /outputs/ and /sample-docs/ directories with README

**Kiro CLI Path (Path 1):**
- [x] Updated analyze.md to handle interactive file loading
- [x] Added explicit file I/O instructions (Read tool → Write tool to /outputs/)
- [x] Updated final delivery messaging for Kiro CLI users
- [x] **Kiro CLI @analyze is now fully functional**

**Flask Web UI Path (Path 2):**
- [x] Completely rewrote ui/app.py to call Claude API instead of subprocess
- [x] Created `load_kiro_context()` function — loads steering docs + prompts as system context
- [x] Created `analyze_document_with_claude()` function — sends document to Claude API
- [x] Created `parse_claude_outputs()` function — extracts three output files from response
- [x] Removed all Kiro subprocess calls
- [x] **Flask → Claude API integration complete**

#### Technical Architecture Summary

**What We Built:**

1. **Kiro CLI Path**
   - Judges run: `kiro-cli` → `@analyze` → provide document path
   - Kiro loads steering docs automatically
   - Orchestrator prompt guides full pipeline
   - Outputs written to /outputs/ directory
   - **Pure Kiro implementation**

2. **Web UI Path**
   - Flask loads Kiro's architecture (steering docs + prompts) as system context
   - User uploads document via browser
   - Claude API processes using same logic as Kiro
   - Returns three outputs to browser
   - **Same intelligence, different interface**

#### The Frustration (Real Talk)

**Days 9-11 were brutal.**
- Kiro wouldn't run headless
- Spent HOURS trying commands that don't exist
- Posted in Discord hoping for answers
- Called developer friends
- Felt completely lost
- Had a working UI with nowhere to plug it in
- Started questioning if I could finish at all

**The breakthrough came from accepting I was blocked and needed a different approach entirely.**

Not a fix. A pivot.

#### Key Decisions

| Decision | Rationale |
|----------|-----------|
| Learn 3 new systems instead of fixing 1 | When truly blocked, change the game |
| Keep the UI at all costs | Emotional validation IS the product, not a nice-to-have |
| Dual-path architecture | Judges test Kiro mastery, parents get compassionate interface |
| Claude API for web path | Same intelligence, different delivery |
| Load Kiro context as system prompts | Maintains architectural consistency across both paths |
| Keep Flask simple | All logic in prompts, Flask just calls API |

#### Why This Decision Was Massive

**Before pivot:**
- Stuck on Kiro headless blocker for 3+ days
- No working product
- Flask UI existed but couldn't connect to anything
- Judges would see a broken demo
- Estimated score: 72-85 points (maybe TOP 10, maybe not)

**After pivot (6 hours later):**
- TWO working paths (Kiro CLI + Web UI)
- Both paths use same Kiro architecture
- Demonstrates Kiro mastery AND real-world application
- UI preserves emotional validation and education
- Non-developers can actually use it
- Estimated score: 85-99 points (competitive for TOP 10)

**The lift:** Going from 1 unknown system to 3 unknown systems in a single day, while not being a developer, with 7 days to deadline.

**Go big or go home.**

#### Scoring Impact

| Criteria | Before Pivot | After Pivot | Delta |
|----------|-------------|-------------|-------|
| Kiro Usage | 12-16 pts | 17-19 pts | +5-7 pts |
| Application Quality | 31-38 pts | 36-40 pts | +5-8 pts |
| Innovation | 10-14 pts | 13-15 pts | +3 pts |
| **Total Estimate** | 72-85 pts | 85-99 pts | **+13-14 pts** |

#### Evening Session (7:00 PM – 8:00 PM) — 🎤 MIC DROP

🎉🎉🎉 **THE UI IS LIVE.** 🎉🎉🎉

**7:25 PM** — Flask Web UI is LIVE at localhost:5000
**7:55 PM** — Confirmed Kiro and Claude Code are reading the SAME files

---

##### What We Accomplished Tonight

**1. UI IS RUNNING ✅**
The Flask web UI is live. Professional design. Clean copy. Working at `127.0.0.1:5000`.

**2. Fixed the Exposure Risk ✅**
Changed "Why I Built This" → "Why This Was Built"

| Before (RISKY) | After (SAFE) |
|----------------|--------------|
| "My attorney asked..." | "The founder's attorney asked..." |
| "My daughter and I were living it" | "A parent and child were living it" |
| "I refused to let anyone else" | "so that no one else has to" |

**Same emotional punch. Safe distance. Legally protected.**

**3. Synced Kiro to the Right Folder ✅**

The Problem:
- Kiro was looking at `dynamous-kiro-hackathon` (old folder, wrong project)
- Claude Code was editing `north-star-high-conflict` (correct folder)
- Two different folders = nothing synced

The Fix:
- File → Open Folder → Desktop → `north-star-high-conflict`
- Now Kiro sees everything Claude Code built

**4. Verified ALL Four Prompts Exist in Kiro ✅**

| Prompt | Status | Content |
|--------|--------|---------|
| analyze.md | ✅ Present | Main orchestrator — runs full pipeline |
| extract-facts.md | ✅ Present | Step 1 — separates facts from emotion |
| map-patterns.md | ✅ Present | Step 2 — maps to 10 predefined patterns |
| generate-outputs.md | ✅ Present | Step 3 — creates 3 audience outputs |

**5. Verified Files Are Synced ✅**

The Test: Search for "founder" in `ui/templates/index.html`
Result: Found "The founder's attorney" — the change Claude Code made 30 minutes earlier.
Conclusion: Same folder. Same files. Two programs reading them.

---

##### What You Learned Tonight — How VS Code, Claude Code, and Kiro Work Together

```
YOUR DESKTOP FOLDER
north-star-high-conflict/
         │
         ├──── VS Code reads/writes here
         │
         ├──── Claude Code reads/writes here
         │
         └──── Kiro reads/writes here (once you open the right folder)
```

**It's like two people editing the same Google Doc.**

One folder = source of truth
Multiple programs = different ways to view/edit it

When Claude Code saves a file, Kiro sees the change.
When Kiro saves a file, Claude Code sees the change.

---

##### Technical Fixes Applied
- Updated Anthropic SDK from 0.18.1 → 0.76.0 (httpx compatibility)
- Updated requirements.txt
- Confirmed Flask loads all Kiro context correctly

---

##### The Moment of the Night

**You:** "I don't trust you (lol)"
**Me:** "Search for 'founder' in the HTML file"
**Kiro:** Shows "The founder's attorney asked" — the EXACT text Claude Code wrote 30 minutes ago
**You:** "FUCKING BRILLIANT"

---

#### Current Status — End of Day 12

**✅ COMPLETED:**
- Both paths architecturally complete
- API integration functional
- Dependencies installed
- File structure ready
- Sample document created (case-001.md)
- **Flask UI running and displaying correctly**
- **Privacy-safe "founder" language applied**
- **Kiro synced to correct folder**
- **All 4 custom prompts verified in Kiro**
- **Files confirmed synced between Claude Code and Kiro**

**⬜ TOMORROW'S PRIORITIES:**
- Test `@analyze` in Kiro CLI
- Test Flask UI pipeline end-to-end (upload → Claude API → outputs)
- Demo video (2-5 min)
- Final README polish
- Submit by Jan 30

**Days Remaining:** 7
**Confidence Level:** HIGH 🚀

---

*End of Day 12. UI live. Files synced. Ending on a win.*

---

## Decision Log

| Date | Decision | Rationale |
|------|----------|-----------|
| Jan 12 | CLI-first architecture | Privacy, simplicity, hackathon demo clarity |
| Jan 13 | Pattern mapping not discovery | Safety constraint — AI matches, doesn't invent |
| Jan 13 | 3×3 output model | Top 3 patterns, up to 3 instances each |
| Jan 13 | Three output files | Different audiences need different framing |
| Jan 14 | Migrate ChatGPT → Claude | Need file creation capabilities, not just chat |
| Jan 15 | Pattern taxonomy from research only | Credibility requires real sources |
| Jan 15 | Build in public on LinkedIn | Visibility + accountability |
| Jan 15 | Map all patterns → narrow to top 3 later | Let the data speak first |
| Jan 16 | Tiered pattern thresholds | Different severities need different evidence bars |
| Jan 16 | UI = vocabulary translation | Core insight: parents need translation, not organization |
| Jan 17 | Strategic weekend rest | Avoid burnout before final push |
| Jan 18 | Personal content on LinkedIn | Building in public = human side too |
| Jan 20 | Product IS the Kiro project | Kiro headless blocker forces pivot |
| Jan 22 | Pivot to Claude Code + VS Code | Tyler's recommendation for code-optimized AI |
| **Jan 23** | **Go from 1 to 3 unknown systems** | **When blocked, change the game — learn Claude Code + VS Code + API** |
| **Jan 23** | **Keep UI at all costs** | **Emotional validation IS the product — fought for this when advised to drop it** |
| **Jan 23** | **Dual-path architecture** | **Serves two audiences: judges test Kiro CLI, parents use compassionate UI** |
| **Jan 23** | **Claude API for web path** | **Same Kiro intelligence, different interface for non-technical users** |

---

## LinkedIn Build-in-Public Posts

| Day | Date | Theme | Status |
|-----|------|-------|--------|
| 1 | Jan 15 | "Stress-test optimism" — absurd math | ✅ Posted |
| 2 | Jan 16 | AI Org Chart (Claude/Perplexity/Kiro/ChatGPT-fired) | ✅ Posted |
| 3 | Jan 18 | Dad's 77th birthday | ✅ Posted |
| 4 | Jan 19 | Karpathy repost — feeling behind | ✅ Posted |
| 5 | Jan 22 | "Struggle Bus Has No Brakes" | ✅ Posted |
| 6 | Jan 24+ | TBD (dual-path breakthrough?) | ⬜ Pending |

---

## Files Committed to GitHub

**Repository:** github.com/ashleycmk/north-star-high-conflict

| Directory | File | Status |
|-----------|------|--------|
| `.kiro/steering/` | product.md | ✅ |
| `.kiro/steering/` | tech.md | ✅ |
| `.kiro/steering/` | structure.md | ✅ |
| `.kiro/agents/` | analyst-agent.json | ✅ |
| `.kiro/prompts/` | analyze.md | ✅ (updated Jan 23) |
| `.kiro/prompts/` | extract-facts.md | ✅ |
| `.kiro/prompts/` | map-patterns.md | ✅ |
| `.kiro/prompts/` | generate-outputs.md | ✅ |
| `reference/` | child-impact-patterns.md | ✅ |
| `ui/` | app.py | ✅ (rewritten Jan 23) |
| `ui/templates/` | index.html | ✅ |
| `ui/static/` | style.css | ✅ |
| root | .gitignore | ✅ (added Jan 23) |
| root | .env.example | ✅ (added Jan 23) |
| root | requirements.txt | ✅ (updated Jan 23) |
| root | README.md | 🟡 Needs polish |
| `docs/` | DEVLOG.md | ✅ (updated Jan 23) |
| `outputs/` | .gitkeep | ✅ (added Jan 23) |
| `sample-docs/` | README.md | ✅ (added Jan 23) |

---

## Remaining Tasks

| Task | Priority | Status |
|------|----------|--------|
| Create sample anonymized document | HIGH | ✅ Complete (case-001.md) |
| Test Kiro CLI path end-to-end | HIGH | ✅ Complete |
| Test Flask web UI path end-to-end | HIGH | ✅ Complete |
| Create 1-2 additional sample documents | MEDIUM | ✅ Complete (case-002, case-003) |
| Demo video (2-5 min) | HIGH | ⬜ Not started |
| Final README polish | MEDIUM | ✅ Complete |
| Final DEVLOG polish for judges | LOW | ✅ Updated through Day 15 |
| Submit to hackathon | HIGH | ⬜ Due Jan 30 |

---

## Time Investment Summary

| Day | Date | Hours | Focus |
|-----|------|-------|-------|
| 1 | Jan 12 (Mon) | ~4 | Research & foundation |
| 2 | Jan 13 (Tue) | ~6 | Architecture & specification |
| 3 | Jan 14 (Wed) | ~7 | Migration & steering docs |
| 4 | Jan 15 (Thu) | ~10 | Pattern taxonomy & first prompt |
| 5 | Jan 16 (Fri) | ~8 | UI, prompts, Flask conversion |
| 6 | Jan 17 (Sat) | ~1 | Strategic rest |
| 7 | Jan 18 (Sun) | ~1 | Personal day + LinkedIn |
| 8 | Jan 19 (Mon) | ~1 | Light day + LinkedIn |
| 9 | Jan 20 (Tue) | ~6 | Resume build, blocker discovery |
| 10 | Jan 21 (Wed) | ~5 | analyze.md, troubleshooting |
| 11 | Jan 22 (Thu) | ~3 | LinkedIn Day 5, Tyler call, decision |
| 12 | Jan 23 (Fri) | ~4.5+ | Claude Code pivot, dual-path build (in progress) |
| **Total** | | **~56.5+** | |

---

## Lessons Learned

### What Worked
1. **Trusting my gut about the UI** — I knew the emotional validation was core value, not optional. Fought for it even when advised to drop it. That insight unlocked the dual-path architecture.
2. **Building in public** — LinkedIn posts created accountability and community support
3. **Strategic rest days** — Avoided burnout, came back stronger
4. **Research-backed pattern taxonomy** — Credibility from real sources, not AI invention
5. **Going big when blocked** — When stuck on 1 system, pivoted to 3 new systems (Claude Code + VS Code + API). Counterintuitive but correct.
6. **Claude Code pivot** — Right tool for the job, faster than struggling with wrong approach
7. **Dual-path architecture** — Turned blocker into innovation opportunity

### What Was Hard
1. **Kiro headless limitation** — Spent days trying to force subprocess integration before pivoting
2. **Tool switching** — ChatGPT → Claude → Claude Code, each migration cost time
3. **Scope creep temptation** — Had to resist adding features beyond MVP

### What I'd Do Differently
1. **Start with Claude Code** — Would have saved 2-3 days of ChatGPT limitations
2. **Test Kiro subprocess earlier** — Would have discovered blocker sooner
3. **Smaller sample docs first** — Don't need massive test cases, just representative ones

---

## Kiro CLI Usage Summary

This section documents how Kiro CLI was used throughout the project development.

### Steering Documents Created

| Document | Purpose | Lines |
|----------|---------|-------|
| `product.md` | Product vision, user journey, success criteria | 81 |
| `tech.md` | Technical architecture, pattern mapping design, safety constraints | 154 |
| `structure.md` | File structure, output formats, naming conventions | ~200 |

### Custom Prompts Developed

| Prompt | Purpose | Size |
|--------|---------|------|
| `analyze.md` | Main orchestrator — runs full 3-step pipeline | 11,667 bytes |
| `extract-facts.md` | Step 1 — separates facts from emotional language | 10,795 bytes |
| `map-patterns.md` | Step 2 — maps facts to 10 predefined patterns | 15,785 bytes |
| `generate-outputs.md` | Step 3 — creates 3 audience-specific outputs | 12,773 bytes |

**Total custom prompt content:** ~51KB of carefully designed instructions

### Agent Configuration

| Agent | Purpose |
|-------|---------|
| `analyst-agent.json` | Non-authoritative analysis agent with strict constraints |

### Kiro CLI Commands Used

| Command | Purpose | When Used |
|---------|---------|-----------|
| `@analyze` | Run full analysis pipeline | Testing, demo |
| `@prime` | Load project context | Development sessions |
| `@code-review-hackathon` | Evaluate against judging criteria | Final review |

### Key Kiro Integration Points

1. **Steering docs guide all behavior** — product.md, tech.md, structure.md define constraints
2. **Custom prompts form the analysis engine** — 4 prompts orchestrate the entire pipeline
3. **Pattern taxonomy as resource** — child-impact-patterns.md (745 lines) referenced by prompts
4. **Agent configuration** — analyst-agent.json enforces non-authoritative positioning
5. **Dual-path architecture** — Kiro CLI path runs natively; Flask path loads same Kiro context

### What Made This a "Kiro Project"

- **The intelligence lives in `.kiro/`** — All analysis logic is in steering docs and prompts, not hardcoded
- **Same prompts power both paths** — Flask loads Kiro's prompts as system context for Claude API
- **Kiro-native workflow** — Developed using Kiro CLI throughout; `@analyze` is the primary interface
- **Steering-driven constraints** — Safety rules (no diagnosis, no legal advice) enforced via steering docs

---

## Day 14 — Monday, January 26 (~1 hour)

### Focus: Developer Call — The Clarity Session

#### The Call That Changed Everything

**Developer friend Declan reviewed the entire project and confirmed:**

> "You've got the meat done. We just need the potatoes."

**What's WORKING:**
- Kiro CLI `@analyze` command → CONFIRMED WORKING
- All 3 outputs generating correctly (attorney, GAL/clinician, internal clarity)
- Prompts, steering docs, pattern taxonomy → ALL SOLID
- Flask UI → RUNNING

**The Simplification:**

Declan stripped away all the complexity I'd been carrying in my head and gave me THREE clear steps:

| Step | What It Does | Status |
|------|--------------|--------|
| **1. File Upload** | User uploads document in Flask UI | ⬜ Not started |
| **2. Run Analysis** | Flask calls the analysis on uploaded file | ⬜ Not started |
| **3. Display Results** | Show the 3 markdown outputs in browser | ⬜ Not started |

**Key Quote:**
> "You can do this in three days, honestly."

**What Declan Saw That I Couldn't:**
- I was overwhelmed by all the moving parts
- He saw a simple input → process → output pipeline
- The architecture is DONE — we just need to connect the dots

#### The Plan for Final Sprint

**Days Remaining:** 3 (deadline Jan 30, 11:59 PM PST)

| Day | Focus |
|-----|-------|
| **Day 14-15** | Build file upload + display results in Flask |
| **Day 16** | Polish, test, record demo video |
| **Day 17** | Final README, submit |

#### Mindset Shift

**Before the call:** Overwhelmed. Anxious. Too many unknowns.
**After the call:** Clear path. Doable timeline. Let's fucking go.

---

## Day 15 — Tuesday, January 27 (~TBD hours)

### Focus: Full System Verification

**Started:** 9:30 AM

#### Flask Web UI Test — PASSED

Ran complete end-to-end test of the Flask Web UI path:

1. Started Flask server (`python3 ui/app.py`)
2. Opened browser to `127.0.0.1:5000`
3. Uploaded `sample-docs/case-001.md`
4. Clicked "Analyze Documentation"
5. **Results displayed in all 3 tabs** ✅

**Analysis Time:** ~2 minutes (acceptable for full pipeline)

#### Zero Fabrication Audit — PASSED

Cross-checked every single fact in the outputs against the source document:

| Pattern | Incidents | Fabrication Check |
|---------|-----------|-------------------|
| Communication Breakdown | 5 | ✅ All verified |
| Boundary Violations | 4 | ✅ All verified |
| Schedule Disruption | 3 | ✅ All verified |

**Key Findings:**
- 12/12 incidents extracted correctly
- All direct quotes verbatim from source
- Pattern grouping logical (Medical + Communication → Communication Breakdown)
- Threshold system working (Negative Parent Portrayal correctly flagged as below 5-incident threshold)
- P1/P2/C1 anonymization working

#### Architecture Clarification

Documented the dual-path architecture:

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

**Why two paths?**
- Kiro CLI has no headless mode (can't be called programmatically)
- Flask loads same steering docs + prompts, calls Claude API directly
- Same intelligence, different interfaces
- Judges see Kiro mastery; end users get accessible web interface

#### Kiro CLI Test — PASSED

Re-tested Kiro CLI path with explicit prompt invocation:

1. Opened Kiro with project folder
2. Asked Kiro to run analysis defined in `.kiro/prompts/analyze.md`
3. Kiro read: analyze.md → case-001.md → child-impact-patterns.md
4. Executed 3-step pipeline
5. **Generated all 3 outputs** ✅

**Analysis Time:** 2m 35s

**Kiro Analysis Summary:**
- 12 facts extracted
- 3 confirmed patterns identified:
  - Medical/Therapeutic Interference (HIGH)
  - Co-Parent Communication Breakdown (HIGH)
  - Schedule & Transition Disruption (MODERATE)
- 2 patterns below threshold (correctly excluded)

#### Status Update

| Path | Status | Test Time |
|------|--------|-----------|
| Kiro CLI | ✅ PASSED | 2m 35s |
| Flask Web UI | ✅ PASSED | ~2 min |

**Both paths produce same quality outputs. Zero fabrication verified.**

#### The Moment

> "Testing in terminal... it's WORKING!!!!!"
>
> "I could fucking cry. This is fucking wild."

Started this hackathon 10 days late, having never written a line of code. Hit wall after wall. Kept going. And now there's a working tool that could actually help parents.

**Remaining Tasks:**
- [x] Test Flask Web UI path ✅
- [x] Test Kiro CLI path ✅
- [x] Create README.md ✅
- [x] Create case-002.md sample document ✅
- [x] Create case-003.md sample document ✅
- [x] Add screenshots ✅
- [x] Add example outputs to repo ✅
- [x] Commit all files to GitHub ✅
- [ ] Record demo video (2-5 min)
- [ ] Submit by Jan 30

#### README Created

Created comprehensive README.md for hackathon judges with:
- Project overview and purpose
- Two-path usage instructions (Kiro CLI + Flask Web UI)
- Architecture diagram
- Pattern taxonomy summary with thresholds
- Project structure
- Setup instructions
- Sample output description
- Safety constraints
- Kiro CLI Features Used section

#### Additional Sample Documents Created

| Document | Incidents | Patterns | Purpose |
|----------|-----------|----------|---------|
| case-001.md | 12 | Medical, Communication | Original test case |
| case-002.md | 28 | Boundary, Coaching, Triangulation | Shows different pattern profile |
| case-003.md | 42 | Financial, Parentification, Distorted | Most complex test case |

#### Screenshots Added

17 screenshots added to `docs/screenshots/` showing:
- Flask UI homepage
- File upload flow
- Analysis processing
- Results display (all 3 tabs)

#### Example Outputs Committed

Example outputs from case-003.md analysis committed to `outputs/` folder so judges can see results without running.

---

## Day 16 — Wednesday, January 28 (~3 hours)

### Focus: Demo Video & Final Polish

**Started:** 12:00 PM

#### Video Script Development

Collaborated with family (my dad!) to develop a compelling video script that leads with emotion and the "why" — not just a feature walkthrough.

**Key insight:** Judges likely have no experience with high-conflict custody situations. The video needs to EDUCATE them on the stakes before showing the product.

**Initial script structure:**
1. **Opening (~45 sec)** — Emotional hook explaining the parent's situation
2. **What It Does (~20 sec)** — Quick explanation of pattern mapping
3. **Flask UI Demo (~90 sec)** — Upload document, show 3 output tabs
4. **Kiro CLI (~20 sec)** — Brief mention of developer path
5. **Closing (~30 sec)** — "Parents find their voice in a system that can silence them"

**Target:** Under 5 minutes

#### README Updates

- Added fallback instructions for Kiro CLI (when `@analyze` triggers spec creation instead of analysis)
- Added sample document table showing all 3 test cases with incident counts and pattern profiles
- Clarified judge instructions for both paths

#### Files Updated

- [x] `docs/VIDEO-SCRIPT.md` — Initial video script with demo paths
- [x] `README.md` — Kiro CLI fallback instructions, sample document table

---

## Day 17 — Thursday, January 29 (~2 hours)

### Focus: Video Recording Attempts

Spent time trying to record the demo video. Multiple takes. The script was good but delivery needed work.

**The struggle:** Recording yourself talking to a camera while also doing a screen demo is harder than it sounds.

---

## Day 18 — Friday, January 30 (~5 hours) — SUBMISSION DAY

### Focus: Final Video Push & Submission

**Started:** Morning

#### Expert Feedback — The Game Changer

Sent the video draft to a friend with extensive hackathon experience. She came back with GOLD:

**Key feedback:**
- Lead with statistics — "Children exposed to high-conflict divorce are 2x more likely to attempt suicide"
- Pre-run the analysis — don't make judges wait on camera
- "One source of truth. Three perspectives." — this became the core framing
- Emphasize that NO OTHER TOOL does this
- Lean into the child impact — this is about protecting CHILDREN
- Parents are the advocates, not attorneys

#### The Final Script — Complete Rewrite

Rewrote the entire script based on feedback:

**New structure:**
1. **Opening (~20 sec)** — Suicide statistics, "mental health crisis hiding in family court"
2. **The Gap (~35 sec)** — "Harm shows up as patterns, not events"
3. **What It Does (~15 sec)** — "North Star is a translator"
4. **Kiro CLI (~15 sec)** — Quick demo, "Kiro is the engine"
5. **Flask UI (~100 sec)** — Pre-loaded results, all 3 tabs, emotional payoff
6. **Closing (~35 sec)** — "North Star doesn't choose sides. It points to what matters most."

**Key lines that landed:**
- "Children exposed to high-conflict divorce are more than twice as likely to attempt suicide in their lives."
- "This is a mental health crisis hiding in family court."
- "Harm rarely shows up as one dramatic event. It shows up as patterns."
- "The child's experience — the most important signal — gets lost in the noise."
- "One source of truth. Three perspectives."
- "Validates what they've been living."
- "North Star doesn't choose sides. It points to what matters most."

#### Video Recording — 3 Hours of Refinement

Spent 3 hours refining and re-shooting the video. Over and over. Worth it for the presentation points.

**Final runtime:** ~3:50

#### Screenshots Organized

Organized 32 screenshots into:
- **13 key screenshots** for judges (renamed with clear names)
- **19 archived** for records

**Coverage:**
- Flask UI: Landing page → File ready → All 3 result tabs
- Kiro IDE: Project structure → Analysis running
- Kiro CLI: Startup → Constraints → Extraction → Mapping → Output → Complete

#### Final Commits

- [x] `docs/VIDEO-SCRIPT.md` — Final script with practice notes
- [x] `docs/DEVLOG.md` — Complete journey documentation
- [x] `docs/screenshots/` — 13 key screenshots, 19 archived
- [x] All outputs, sample docs, README verified

---

## Submission Complete

**Final Time Investment:**

| Day | Date | Hours | Focus |
|-----|------|-------|-------|
| 1 | Jan 12 (Sun) | ~4 | Research & foundation |
| 2 | Jan 13 (Mon) | ~6 | Architecture & specification |
| 3 | Jan 14 (Tue) | ~7 | Migration & steering docs |
| 4 | Jan 15 (Wed) | ~10 | Pattern taxonomy & first prompt |
| 5 | Jan 16 (Thu) | ~8 | UI, prompts, Flask conversion |
| 6 | Jan 17 (Fri) | ~1 | Strategic rest |
| 7 | Jan 18 (Sat) | ~1 | Personal day + LinkedIn |
| 8 | Jan 19 (Sun) | ~1 | Light day + LinkedIn |
| 9 | Jan 20 (Mon) | ~6 | Resume build, blocker discovery |
| 10 | Jan 21 (Tue) | ~5 | analyze.md, troubleshooting |
| 11 | Jan 22 (Wed) | ~3 | LinkedIn Day 5, Tyler call |
| 12 | Jan 23 (Thu) | ~6 | Claude Code pivot, dual-path build |
| 13 | Jan 25 (Sat) | ~1 | Recovery & planning |
| 14 | Jan 26 (Mon) | ~1 | Declan call, simplification |
| 15 | Jan 27 (Tue) | ~4 | Full system verification |
| 16 | Jan 28 (Wed) | ~3 | Video script with family |
| 17 | Jan 29 (Thu) | ~2 | Video recording attempts |
| 18 | Jan 30 (Fri) | ~5 | Final video, screenshots, submission |
| **Total** | | **~74** | |

---

## Why This Tool Exists

Children exposed to high-conflict divorce are more than twice as likely to attempt suicide — and 48% more likely to have suicidal thoughts that follow them into adulthood.

Children exposed to ongoing high conflict show depression, anxiety, PTSD, and conduct problems that worsen — not improve — after the divorce is finalized.

It is a mental health crisis hiding in family court, and something must be done to help advocate for these children.

Parents in these situations are told to document. They do. They have years of notes, texts, emails. But when their attorney asks for "10 examples of harmful behavior affecting the child" — they're paralyzed.

**What do you pull from hundreds of entries?**
**What will the attorney take seriously?**
**What will the GAL take seriously?**
**What will the court act on?**

No one tells them. No tool helps them. They sit in silence, wondering if what they're seeing is even real.

**North Star was built to end that silence.**

It doesn't diagnose. It doesn't give legal advice. It doesn't choose sides.

It translates. It maps lived experience to patterns that professionals recognize. It gives parents the vocabulary to advocate for their children.

*"You know something is wrong. You just don't know what to call it."*

This tool exists because children deserve protection — and the parents who see what's happening deserve to be heard.

---

## The Helpers

This project wouldn't exist without the people who jumped in when it mattered.

| Person | Role | Key Contribution |
|--------|------|------------------|
| **Tyler Nelson** | Developer friend | "Use Claude Code. Use VS Code." The phone call that changed everything. |
| **Declan** | Developer friend | "You've got the meat done. We just need the potatoes." Saw the clear path when I couldn't. |
| **Alexandra Dmytriw** | Girlfriend | Video feedback: lead with statistics, pre-run the demo, story wins. Turned out she had extensive hackathon experience — I had no idea. |
| **Justin** | Developer (AI accelerator) | Kiro integration troubleshooting, confirmed chat interface is standard approach. |
| **Dad** | Family | Day 16 video script collaboration. "Lead with the why." |

---

## The Emotional Arc

```
Day 1:  Excited. Optimistic. Maybe unreasonably so.
        ↓
Day 3:  Fired ChatGPT. Caught it fabricating.
        ↓
Day 5:  BREAKTHROUGH. The positioning insight clicked.
        ↓
Day 6:  Strategic rest. "The delusion is load-bearing at this point."
        ↓
Days 9-11: THE WALL. Kiro won't run headless. Questioning everything.
        ↓
Day 11: Tyler call. "Use Claude Code." Laughed out loud.
        ↓
Day 12: Pivot and trust. "FUCKING BRILLIANT."
        ↓
Day 14: Declan call. Clarity. "You can do this in three days."
        ↓
Day 15: VERIFICATION. Both paths working. "This is fucking wild."
        ↓
Day 18: Submission. Ohmyfuckinggod we did it.
```

---

**Submitted:** Friday, January 30, 2026

*"The optimistic delusion was load-bearing. And it held."*

🚀
