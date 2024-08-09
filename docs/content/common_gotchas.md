# Common Gotchas

If you are encountering problems with a codebase rendered from this template, perhaps one of the
following is happening:

## Configuring PyPI and TestPyPI

### **'Entire account'-scoped secrets**

'Entire account'-scoped tokens for *PyPI* (and *TestPyPI*) are not ideal, but there is a cold start problem when adding new projects to your account: you need a token to add a new project, but you need a project to create a project-scoped token.  For this reason, you need to create and configure GitHub with a temporary 'Entire account'-scoped token first, and then when you have added the project to *PyPI* and *TestPyPi*, you need to delete the temporary token and repeat the process: create a token scoped to the project and reconfigure *GitHub* with the new secret.  **It's easy to forget to do this.**

## Workflow Issues

### **My checks keep failing**

Have you given workflows write permissions?  If not, navigate within the repo to `Settings->Actions->General` and select `Read and write permissions`.

## Developing Documentation

### **I've added a new markdown file to the `docs/content` directory, but it isn't showing-up in the final rendered documentation**

Have you added it to the `docs/index.rst` file?  Follow the examples there for adding your new content
to the documentation.
