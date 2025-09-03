# Repository Guidelines

## Project Structure & Module Organization
- Root: `README.md` (overview) and `LICENSE`.
- Source: place new code under `src/` (create if missing). Keep shared helpers in `src/lib/` or `src/utils/`.
- Examples: runnable samples in `examples/` with one feature per file (e.g., `examples/chat_basic.py`, `examples/chat-basic.ts`).
- Tests: `tests/` mirroring source paths (e.g., `tests/examples/…`).
- Scripts: dev helpers in `scripts/` (setup, lint, release).
- Assets: non-code files in `assets/`.

## Build, Test, and Development Commands
Use the stack appropriate to your example; prefer simple, zero-config scripts.
- Node.js
  - `npm install`: install deps
  - `npm run dev`: run local sample (document the target in README)
  - `npm test`: run Jest tests
  - `npm run lint` / `npm run format`: ESLint/Prettier
- Python
  - `python -m venv .venv && source .venv/bin/activate`
  - `pip install -r requirements.txt`
  - `pytest -q`: run tests
  - `ruff check .` / `black .`: lint/format

## Coding Style & Naming Conventions
- JavaScript/TypeScript: 2-space indent, semicolons on, Prettier + ESLint (`standard` or `eslint:recommended`).
- Python: 4-space indent, type hints where useful, Black + Ruff.
- Names: `camelCase` variables/functions, `PascalCase` classes, `SNAKE_CASE` constants; Python modules as `snake_case.py`.
- Files: example names should describe capability (e.g., `streaming_chat.ts`).

## Testing Guidelines
- Frameworks: Jest (Node) or Pytest (Python).
- Coverage: target ≥80% for new/changed code.
- Test names: co-locate under `tests/` using `*.spec.ts` / `test_*.py`.
- Include at least one happy-path and one failure-path test.

## Commit & Pull Request Guidelines
- Commits: follow Conventional Commits (e.g., `feat: add streaming chat sample`).
- PRs: include a clear description, linked issue (if any), steps to run, and sample output (logs or `curl`). Keep scope small and focused. Ensure CI/tests pass.

## Security & Configuration Tips
- Never commit secrets. Read `OPENAI_API_KEY` from environment (e.g., `.env` loaded via `dotenv`). Provide `.env.example` with placeholder keys.
- Handle rate limits/timeouts with retries and backoff in examples; avoid long-lived secrets in code/comments.

## Architecture Notes
- Keep each example self-contained. Factor reusable logic (auth, client setup) into `src/lib/` to avoid duplication and simplify docs.
