# Starting a new Python codebase?
This template takes the effort out of starting from a good place.

## Getting Started
***Make sure Cookiecutter is installed...***
``` console
pip install cookiecutter
```
*(or better yet, use [pipx](https://pypa.github.io/pipx/))*
``` console
pipx install cookiecutter
```
***...use it to render the project...***
``` console
cookiecutter gh:ADACS-Australia/adacs_template_python_base

```
***...answer the questions...***

![ADACS Python Template Questions](https://github.com/ADACS-Australia/adacs_template_python_base/blob/main/docs/assets/adacs_python_template_cookiecutter_questions.png?raw=true)

***...and configure the services you need using [these instructions](https://adacs-template-python-base.readthedocs.io/en/latest/content/configuring_services.html).***

## What do you get for this?
***A codebase that eases collaboration and automatically:***
* Ensures that all commits on the main branch and released versions build correctly and pass all unit tests
* Enforces code formatting and linting policies
* Manages code and release versioning
* (optionally) publishes your code to PyPI so people can easilly install it
* (optionally) updates, builds and publishes documentation to *Read the Docs*.

***Other ADACS Python templates can then be applied to this base template to quickly kickstart a new project.***

