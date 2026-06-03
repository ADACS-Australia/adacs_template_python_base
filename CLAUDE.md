# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Project Is

This is a **Cookiecutter template** for generating new Python projects. It is not a conventional Python package — the `{{cookiecutter.repo_name}}/` directory contains the Jinja2-rendered template that gets instantiated when users run `cookiecutter`. The Python package in `python/adacs-template-python-base/` is minimal scaffolding for the template tool itself.

## Commands

Install dependencies (requires Python >= 3.13 and Poetry):
```console
poetry install
```

Run the test suite:
```console
pytest
```

Run a single test:
```console
pytest tests/test_bake_project.py::test_bake_with_defaults
```

Run tests in Docker (recommended — avoids venv pollution and state bleed between test runs):
```console
make docker-build
make docker-tests
```

Lint (Ruff) and format (Black):
```console
poetry run ruff check .
poetry run black .
```

Type check:
```console
mypy --explicit-package-bases python
```

Build docs locally:
```console
make docs
# Then open docs/_build/html/index.html
```

Install pre-commit hooks:
```console
pre-commit install
```

## Architecture

### Template structure

- `{{cookiecutter.repo_name}}/` — the Jinja2 template directory that Cookiecutter renders into a new project. Files here are excluded from linting, Black, mypy, and pytest because they may contain intentionally invalid Python (Jinja2 syntax).
- `cookiecutter.json` — defines template variables and their defaults. Private variables (prefixed `__`) are computed from user inputs and not prompted.
- `hooks/` — Python scripts run by Cookiecutter before (`pre_gen_project.py`) and after (`post_gen_project.py`) rendering. **These files are Jinja2 templates themselves**, so they can contain invalid Python syntax — avoid auto-formatting them. `post_gen_project.py` initialises a git repo, makes an initial commit, and prints setup instructions from `INSTRUCTIONS.template`.
- `local_extensions/__init__.py` — custom Jinja2 extensions registered in `cookiecutter.json`: `CurrentYearExtension`, `UnderlineExtension`, `PascalCaseExtension`, `EscapeQuotes`. Any non-stdlib imports here must be available to the user's `cookiecutter` installation.

### Testing

Tests use `pytest-cookies` to bake the template into a temp directory and then verify the rendered project. Two test files:
- `tests/test_bake_project.py` — structural checks (files present, year in LICENSE).
- `tests/test_template.py` — functional checks: installs the baked project into its own venv and runs `poetry check`, `pytest`, `make docs`, `black`, and `ruff` inside it.

`tests/utils.py` provides `bake_in_temp_dir` (bakes + cleans up), `run_inside_dir` (runs a command inside a path, optionally activating the baked project's `venv/`), and helpers.

Running `test_template.py` tests create venvs and install packages, which can bleed state between runs. Run these in Docker to keep each bake isolated.

### CI/CD (GitHub Workflows)

- `pull_request.yml` — linting, formatting, build, docs, and tests on every PR.
- `bump.yml` — auto-increments semver tag on every push to `main`. Add `[version:minor]` or `[version:major]` to the PR head commit message to control which component is bumped; default is patch.
- `publish.yml` — triggered by a GitHub Release; publishes to PyPI and rebuilds Read the Docs.

Versioning uses `poetry-dynamic-versioning` (reads from git tags). Local dev shows `v0.0.0-dev`.

### Key constraints

- `{{cookiecutter.repo_name}}/` and `hooks/` are excluded from Black, Ruff, and mypy — do not remove those exclusions.
- `pytest` is configured with `--ignore={{cookiecutter.repo_name}}` so template Python files are never imported during the test run.
- Direct commits to `main` are blocked by a pre-commit hook (`no-commit-to-branch`); all changes go via PR.
- Template dependencies (`rich`, `cookiecutter`) must be installable from the user's `cookiecutter` environment, not just from this repo's venv.
