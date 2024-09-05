(template-maintenance)=
# Maintaining This Template

Developers maintaining this template codebase should be aware of the development guidelines presented [here](#development-guidelines).  This section discusses issues specific to
the maintenance of this template.

## Some things to note about Cookiecutter templates

The following are some things that you might not know about Cookiecutter templates that you may need to be aware of if you are
developing on this template:

### Hooks

There are two files in the `hooks` directory: one which gets run *before* a tempalte gets rendered and one which gets run *after* a template gets rendered.  **Both of these files are actually Jinja2 templates.**  As a result, these files can legitimately possess invalid code.  **Be particularly careful if your code editor is configured to autoformat code, since this can cause unintended bugs in these files.**

### Dependencies

If any code in the `local_extensions` or `hooks` directories import packages that are not part of the Python standard library, the user will need to have those packages installed when they attempt to render the template.  If they installed `cookiecutter` with `pipx` then this can be done as follows (for a dependency named `dependency_name`):
``` console
pipx inject cookiecutter dependency_name
```

Otherwise they should install the dependency into the directory they
installed `cookiecutter` into as follows:
``` console
pip install dependency_name
```

Make sure they are alerted to this issue in the documentation and provided instructions for installing the needed dependencies.  This is particularly important in the *Getting started* section of the README.

## Changes to documentation

Make sure that any changes that get made to the template are reflected in the
documentation.  Things to pay attention to are:

1. The project and template READMEs
2. The INSTRUCTIONS.template file
3. The documentation in both this codebase and in the template
