# AGENTS.md: Persistent notes for opencode agents across sessions/projects

## Project Intent

This repository is a Python library for quickly creating networks of Docker containers used as ranges for hackathons or cybersecurity capability benchmarks.

**Agent Directives:**
- Produce professional-grade code: full type annotations (mypy strict), tests &gt;80% coverage (pytest), docstrings, no hacks/suppresses.
- Follow mature Python lib standards: Black/Ruff formatting, semantic versioning, pyproject.toml structure.
- Designed for reuse: clear API, examples/tests, CLI support.
- Zero AI slop: human-readable, maintainable, robust.

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

Last updated: Thu Apr 23 2026
