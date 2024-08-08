# Maintaining This Template

Developers maintaining this template codebase should be aware of the development
guidelines presented [here](#developing-new).  This section discusses issues specific to
the maintenance of this template.

## Running tests

When testing, temporary projects get created and need to be installed into an environment before tests can be run, documentation builds checked, etc.  Be warned that this can both pollute your development environment and lead to unreliable tests due to the bleeding of state from past test runs to new runs.

To address this, a `Dockerfile` and `Makefile` are provided for running tests in a container.  Run the
following to build the container:

``` console
make docker-build
```

Run the following to run the tests in the container:

``` console
make docker-tests
```

::: {note}
Running the tests in a container on MacOS is **slow**: 10 mins on an M1 Mac vs 1 min in the CI/CD.  Optimisation suggestions welcome.
:::

## Some things to note about Cookiecutter templates

The following are some things that you might not know about Cookiecutter templates that you may need to be aware of if you are
developing on this template:

### Hooks

There are two files in the `hooks` directory: one which gets run *before* a tempalte gets rendered and one which gets run *after* a template gets rendered.  **Both of these files are actually Jinja2 templates.**  As a result, these files can legitimately possess invalid code.  **Be particularly careful if your code editor is configured to autoformat code, since this can cause unintended bugs in these files.**

## Changes to documentation

Make sure that any changes that get made to the template are reflected in the
documentation.  Things to pay attention to are:

1. The project and template READMEs
2. The INSTRUCTIONS.template file
3. The documentation in the template and this documentation here
