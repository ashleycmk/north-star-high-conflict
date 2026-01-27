# Sample Documents

This directory contains anonymized sample documentation for testing North Star analysis.

## Running Analysis

### Using Kiro CLI (Recommended for Judges)

1. Start Kiro:
   ```bash
   kiro-cli
   ```

2. Load the analyzer:
   ```
   @analyze
   ```

3. When prompted, provide the full path to a sample document:
   ```
   /Users/ashley/Downloads/north-star-high-conflict/sample-docs/case-001.md
   ```

4. Review outputs in `/outputs/` directory

### Using Web UI

1. Start the Flask server:
   ```bash
   cd ui
   python app.py
   ```

2. Open http://localhost:5000

3. Upload a sample document from this directory

4. Review results in the browser

## Sample Files

- **case-001.md** - Medical/communication documentation example (coming soon)
- More samples will be added after anonymization

## Anonymization Notice

All sample documents use:
- Role identifiers: Sarah (P1), Michael (P2), Ethan (C1)
- Generic locations: Metro County, Riverside, etc.
- Date-shifted timelines (offset by 8 months from original)
- Gender-swapped to protect identity (daughter → son)

These are based on real custody documentation but have been fully anonymized for demonstration purposes.
