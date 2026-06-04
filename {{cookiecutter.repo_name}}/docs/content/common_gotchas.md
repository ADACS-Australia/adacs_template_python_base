# Common Gotchas

If you are encountering problems with this project, perhaps one of the following is happening:

## Configuring PyPI and TestPyPI

### 'Entire account'-scoped tokens

'Entire account'-scoped tokens for *PyPI* (and *TestPyPI*) are not ideal, but there is a cold start problem when adding new projects to your account: you need a token to add a new project, but you need a project to create a project-scoped token.  For this reason, you need to create and configure GitHub with a temporary 'Entire account'-scoped token first, and then once the project has been published to *PyPI* for the first time, delete that token, create a new one scoped to just this project, and update the *GitHub* secret.  **It's easy to forget to do this second step.**

## Workflow Issues

### My checks keep failing

Have you given workflows write permissions?  If not, navigate within the repo to `Settings->Actions->General` and select `Read and write permissions`.

### I pushed directly to `main` and nothing worked as expected

Direct pushes to `main` bypass the pull request workflow, which means the automated version bump and any branch-protection checks are skipped.  Always work on a feature branch and merge via a Pull Request.  If branch protection rules are configured (see [Configuring Services](#configuring-github)), GitHub will prevent direct pushes automatically.

## Developing Documentation

### I've added a new Markdown file to `docs/content/` but it isn't appearing in the rendered docs

Have you added it to `docs/index.rst`?  Sphinx only renders files that are listed in the `toctree`.  Follow the existing entries in that file as a guide, and place your new file in the order you want it to appear.
