# Maintaining This Template

Developers maintaining this template codebase should be aware of the development
guidelines presented [here](#developing-new).  This section discusses issues specific to
the maintenance of this template.

## Running tests

When testing, temporary projects get created and need to be installed into an environment before tests can be run, documentation builds checked, etc.  Be warned that this can both pollute your development environment and lead to unreliable tests due to the bleeding of state from past test runs to new runs.

To address this we will soon add the ability to run tests in a Docker container, where we can ensure fresh and reproducable test runs.  This is not implemented yet but will be soon.

## Some things to note about Cookiecutter templates

The following are some things that you might not know about Cookiecutter templates that you may need to be aware of if you are
developing on this template:

### Hooks

There are two files in the `hooks` directory: one which gets run before a tempalte gets rendered and one which gets rendered after a template gets rendered.  **Both of these files are actually Jinja2 templates.**  As a result, these files can actually possess invalid code.  They do not get automatically formatted or linted as a result, so please be careful when developing these files; try to maintain proper coding style, for example.

## Changes to documentation

Make sure that any changes that get made to the template are reflected in the
documentation.  Things to pay attention to are:

1. The project and template READMEs
2. The INSTRUCTIONS.template file
3. The documentation in the template and this documentation here
