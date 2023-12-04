# Starting a new Python codebase?
This template takes the effort out of starting from a good place.

## Getting Started
***Make sure Cookiecutter is installed...***
``` console
$ pip install cookiecutter
```
*(or better yet, use [pipx](https://pypa.github.io/pipx/))*
``` console
$ pipx install cookiecutter
```
***...use it to render the project...***
``` console
$ cookiecutter gh:gbpoole/adacs_python_template

```
***...answer the questions...***

![ADACS Python Template Questions](https://github.com/gbpoole/adacs_python_template/blob/main/docs/assets/adacs_python_template_cookiecutter_questions.png?raw=true)

***...and configure the services you need using [these instructions](https://adacs-python-template.readthedocs.io/en/latest/content/configuring_services.html).***

## What do you get for this?
***A codebase that eases collaboration and automatically:***
* Enforces code formatting and linting policies
* Ensures that all commits on the main branch and released versions build correctly and pass all unit tests
* (optionally) publishes your code to PyPI so people can easilly install it
* (optionally) updates, builds and publishes documentation to *Read the Docs*.
