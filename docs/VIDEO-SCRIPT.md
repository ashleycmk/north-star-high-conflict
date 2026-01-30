# North Star Demo Script — FINAL

**Hackathon Submission Video (~4 minutes)**

---

## OPENING (~20 sec)

"Children exposed to high-conflict divorce are more than twice as likely to attempt suicide in their lives.

This is a mental health crisis hiding in family court.

Parents document hundreds of incidents — because they're taught to. But they have no idea how to communicate what they're seeing, and how to advocate for their children."

---

## THE GAP (~35 sec)

"An attorney asks for ten examples of harmful behavior affecting the child. Ten — out of hundreds of notes, texts, emails that span years.

Harm rarely shows up as one dramatic event. It shows up as patterns. And those patterns are buried across documents no one has time to synthesize.

And the child's experience — the most important signal — gets lost in the noise.

Nothing existed, before today, to do this clearly, consistently, and safely.

No other tool does this."

---

## WHAT IT DOES (~15 sec)

"North Star is a translator. Mapping lived experiences to ten research-backed behavioral patterns, that professionals recognize as harmful to children.

One source of truth gets translated for three different audiences. Let me show you."

---

## KIRO CLI — The Engine (~15 sec)

*[Switch to Kiro terminal]*

**Kiro CLI Demo Commands:**
```bash
# Step 1: Open Terminal
# Step 2: Navigate to project
cd ~/Desktop/north-star-high-conflict
kiro-cli
@analyze
/Users/ashley/Desktop/north-star-high-conflict/sample-docs/case-002.md
```

"The intelligence lives in Kiro — steering documents, custom prompts. This is the engine."

---

## DEMO — Flask UI (~100 sec)

*[Switch to Flask UI with results already loaded]*

"This is the web interface — what a parent would actually use.

I uploaded a sample document. Twenty-eight incidents over two years. The analysis took about two minutes — reading every incident, extracting facts, and mapping them to patterns.

Three outputs for three audiences."

*[Click Attorney tab]*

"The Attorney Summary — facts only. No emotion, just evidence."

*[Click GAL & Therapist tab]*

"The GAL and Clinician Summary. Quick context — a guardian ad litem is a third attorney often brought into high-conflict cases specifically to represent the child's best interests. This output is framed around child impact — what the child is experiencing."

"Every date and quote the system has pulled, come verbatim from the documentation. Strict zero-fabrication boundaries. Every fact pulled directly from the source."

*[Click Internal Clarity tab]*

"And Internal Clarity — this is for the parent. It validates what they've been living. It explains WHY each pattern was surfaced. It shows evidence quality scores.

And notice the disclaimer built right in — this is orientation, not authority. It does not replace your legal team. That's important — parents need to understand what this tool IS and what it ISN'T.

This is how parents learn to understand their own documentation."

"Most importantly — it focuses on the child. Not who's winning the conflict."

---

## CLOSING — Why It Matters (~35 sec)

*[Back to camera]*

"Parents in high-conflict situations are often the primary witness.

They're told to document. But no one teaches them how to communicate what they're seeing.

North Star gives them CLARITY and the vocabulary to advocate for their children.

North Star doesn't choose sides. It points to what matters most.

That's North Star."

---

**TOTAL RUNTIME: ~3:50**

**New order:** Opening → Gap → What It Does → Kiro (quick) → Flask UI (emotional payoff) → Closing

---

## QUICK REFERENCE

### Statistics used:
- 2x more likely to attempt suicide
- 48% more likely to carry suicidal thoughts into adulthood

### Key phrases hit:
- "Mental health crisis hiding in family court"
- "Invisible, cumulative, lifelong"
- "Because they're told to" (document)
- "Harm rarely shows up as one dramatic event — it shows up as patterns"
- "The child's experience — the most important signal — gets lost in the noise"
- "Nothing exists to bridge that gap"
- "Synthesize all of that clearly, consistently, and safely"
- "No other tool does this"
- "North Star is a translator"
- "Surfacing risk to children before harm escalates"
- "Articulate concerns without inflammatory language — often for the first time"
- "One source of truth. Three perspectives."
- "Validates what they've been living"
- "Orientation, not authority" / "Does not replace your legal team"
- "Focuses on the child — not who's winning the conflict"
- "Kiro is the engine"
- "In high-conflict divorce, clarity protects children"
- "North Star doesn't choose sides. It points to what matters most."

### Child quotes read aloud:
- "Sometimes I feel like a spy."
- "I don't want to choose. Why does everyone want me to choose?"

### Demo elements:
- Pre-loaded results (no waiting)
- All three tabs shown with explanations
- GAL role explained briefly
- Internal Clarity — validates, educates, shows disclaimer built into tool
- Pattern 1 in detail (GAL view)
- Kiro CLI shown running

---

## PRACTICE NOTES

**Opening stats** — Say both stats, then pause briefly before "This is a mental health crisis." Let the numbers land.

**"Because they're told to"** — This is the tragedy. They did what they were supposed to do. It still isn't enough.

**"Harm rarely shows up as one dramatic event"** — This EDUCATES the judges. Slow down here.

**"The child's experience — the most important signal — gets lost in the noise"** — Land this line. It's powerful.

**"Often for the first time"** — In the translator section. Parents have never been able to do this before.

**Internal Clarity explanation** — "Validates what they've been living" — say with weight. Then point to disclaimer.

**Child quotes** — Read these SLOWLY. These are the knockout punch. Don't rush.

**"That's a nine-year-old"** — Brief pause after.

**"Focuses on the child — not who's winning the conflict"** — Addresses skepticism. Important line.

**Closing sequence** — Three punches:
1. "Clarity protects children" (thesis)
2. "Doesn't choose sides. Points to what matters most." (skepticism-killer)
3. "That's North Star." (clean end)

---

## DEMO FILE PATH

```
/Users/ashley/Desktop/north-star-high-conflict/sample-docs/case-002.md
```

## KIRO COMMAND (if needed)

```
Please run the analysis defined in .kiro/prompts/analyze.md on the document at sample-docs/case-002.md
```
