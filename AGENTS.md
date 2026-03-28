# AGENTS.md: Persistent notes for opencode agents across sessions/projects

## Tool Usage Notes
- **String Escaping in XML Tools**: NEVER use \\\" or escaped quotes in `write`/`edit` newString/oldString. Use raw `"""` or `'''` for docstrings/multiline. XML parser handles it; escapes cause syntax errors in code.
  - Bad: \\\"\\\"\\\"Doc\\\"\\\"\\\"
  - Good: \"\"\"Doc\"\"\"

## Testing Verification
- ALWAYS check test collection first: `uv run pytest --collect-only` (confirm expected # tests).
- Run `uv run pytest -v -ra` to verify passes/fails/skips (positive presence, not just no errors).
- Update tests post-impl; aim 80%+ coverage.

- **Python Edits**: Mimic existing style (indent, types, docstrings). Read file first.

- **Git**: Stage with `git add -A`; commit only on request.

## Commands
- Lint: uv run ruff check .
- Typecheck: uv run mypy .
- Test: uv run pytest

Last updated: 2026-03-27
