## Rightly Stage 0

1. Create a virtual environment:
   ```
   python -m venv .venv
   .\.venv\Scripts\activate   # Windows
   # source .venv/bin/activate  # macOS/Linux
   ```
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run CLI:
   ```
   python -m rightly_stage0.cli harvest il_disability_general_mental
   ```

Folder structure:
- src/rightly_stage0/: source code
- tests/: tests
- .env.example: environment variables example (copy to .env and fill in values)