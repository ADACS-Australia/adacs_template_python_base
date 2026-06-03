# Contributing

Thank you for your interest in contributing to **{{cookiecutter.project_name}}**.

## Where to find the detailed guidelines

Full development guidelines — including how to set up the code locally, run tests, write documentation, and create releases — are in the project documentation:

```
docs/content/development_guidelines.md
```

or, once the docs are built, under the **Development Guidelines** section of the rendered documentation.

## Quick-start workflow

1. **Branch** — create a feature branch off `main`; never commit directly to `main`.
2. **Develop** — install dependencies with `poetry install`, run tests with `pytest`.
3. **Commit** — write clear, descriptive commit messages. If your change adds new functionality, include `[version:minor]` in the head commit message; for breaking changes use `[version:major]` (patch is the default).
4. **Open a PR** — fill in every section of the pull request template and tick all applicable checklist items before requesting review.

## Pre-commit hooks

This project ships pre-configured git hooks. Install them once with:

```console
poetry run pre-commit install
```

They run linting and formatting checks locally, catching issues before CI does.

## Reporting issues

Please open a GitHub Issue with a clear description of the problem and, where possible, a minimal reproducible example.
