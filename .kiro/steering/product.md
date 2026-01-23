# Product Overview

# Product Overview

## Product Purpose
**North Star for High-Conflict Cases** is a CLI-first tool that helps parents translate emotionally overwhelming documentation into clear, restrained, child-centered summaries for professional review in high-conflict custody contexts.

The product exists to orient attorneys, guardians ad litem (GALs), and child-focused clinicians toward concrete child-impact information, without emotional noise, narrative escalation, or interpretive overreach.

This system provides orientation, not authority. It does not offer legal advice, diagnosis, or strategy, and does not replace attorneys, GALs, or clinicians.

The system is accessed via a minimal local user interface designed for non-technical users to upload a single document and generate outputs. The CLI remains the core execution engine and source of truth.

## Target Users
### Primary Users
- Parents or advocates preparing documentation for professional review in high-conflict custody situations

### Downstream Professional Readers
- Family law attorneys  
- Guardians ad litem (GALs)  
- Child-focused clinicians or therapists  

### Core User Needs
- Reduce emotional and cognitive overload from extensive documentation  
- Separate factual statements from emotional interpretation  
- Identify concrete, defensible examples of child impact  
- Maintain neutral, professional framing  
- Avoid escalation, strategy, or diagnostic language that harms credibility 

## Key Features
- CLI-based ingestion of a single text or markdown document
- Explicit separation of factual content from emotional language
- Intra-document pattern identification
- Perspective-based relevance analysis using professional review lenses for:
  - Attorney
  - GAL
  - Clinician/Therapist
- Convergence on up to three core child-impact patterns, each supported by concrete, fact-only instances
- Three structured outputs:
  1. Attorney-facing factual summary (facts only, neutral tone)
  2. GAL / clinician child-impact summary (contextual but factual)
  3. Internal clarity view explaining why examples were prioritized

## Design Constraints
- Single-document analysis only
- No fabrication or gap-filling; missing information is flagged, not inferred
- Patterns require multiple supporting instances to be surfaced
- Deterministic, repeatable outputs for identical inputs
- Patterns are surfaced to support professional review, not to label behavior or draw conclusions.

## Business Objectives
- Help users narrow large volumes of documentation into **fewer, stronger, credibility-preserving examples**  
- Reduce noise and repetition so professional reviewers can assess child impact more efficiently  
- Support restraint and clarity in emotionally charged situations  
- Complement existing legal and educational guidance rather than replace it  
- Provide a repeatable, transparent process that prioritizes child wellbeing over narrative escalation  

## User Journey
1. The user provides a single document containing notes, logs, or written observations related to a high-conflict custody situation.
2. The system separates factual statements from emotional or interpretive language.
3. Recurring patterns related to child impact are identified within the document.
4. The system evaluates patterns through multiple professional relevance lenses (attorney, GAL, clinician).
5. Up to three core patterns are selected based on relevance and credibility.
6. Each pattern is supported by up to three concrete, fact-only instances.
7. The user receives three structured outputs tailored to different audiences.


## Success Criteria
- A single CLI command reliably generates all three outputs.
- Outputs surface no more than three clearly defined patterns, each supported by concrete instances.
- Professional-facing summaries remain neutral, factual, and restrained.
- Emotional, strategic, or diagnostic language is excluded from professional outputs.
- Large, unstructured inputs are consistently narrowed into a credible, reviewable set of examples.
- Judges or reviewers can understand the purpose, boundaries, and value of the tool in under two minutes.
### Parent-Facing Success Criteria
- The user feels less overwhelmed after running the tool.
- The user can clearly see which patterns matter most and why.
- The user is able to reduce large volumes of notes into a smaller, more credible set of examples.
- The user gains confidence that the outputs are neutral, factual, and appropriate to share with professionals.
- The user understands how restraint and prioritization protect credibility in high-conflict situations.
- Outputs reduce the risk of over-documentation or credibility loss for the user.