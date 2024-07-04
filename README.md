# Starting a new Python codebase?
This template takes the effort out of starting from a good place.

## Getting Started
***Installing the needed dependencies and building your new project is easy with the following steps ...***

### Make sure Cookiecutter is installed
``` console
pip install cookiecutter
```
*(or better yet, use [pipx](https://pypa.github.io/pipx/))*
``` console
pipx install cookiecutter
```

### Make sure Poetry is installed
Use the official installer
``` console
curl -sSL https://install.python-poetry.org | python3 -
```
*(or better yet, use [pipx](https://pypa.github.io/pipx/))*
``` console
pipx install poetry
```

### Render the project
Run cookiecutter on the template's repository:
``` console
cookiecutter gh:ADACS-Australia/adacs_template_python_base
```
and answer the questions:

![ADACS Python Template Questions](https://github.com/ADACS-Australia/adacs_template_python_base/blob/main/docs/assets/adacs_python_template_cookiecutter_questions.png?raw=true)

### Install the new project
Create and activate a new virtual environment (**use Python version >= 3.11**) using your favourite method (if you don't know how to use Python environments, we advise you to go learn about them now) and install the project by running the following in the new repo directory:
``` console
poetry install
```

### Configure the services you need
Follow [these instructions](https://adacs-base-python-template.readthedocs.io/en/latest/content/configuring_services.html) to
configure GitHub, Read the Docs, PyPI, etc.

## What do you get for this?
***A codebase that eases collaboration and automatically:***

* Ensures that all code on the main branch and released versions:
    * builds correctly (including documentation) and passes all unit tests
    * conforms to the project's code formatting and linting policies
    * is properly versioned

* And optionally, automates the following for new releases of your project:
    * publication to [PyPI](https://pypi.org) so people can easilly install it
    * publication of updated documentation to *Read the Docs*

***Other ADACS Python templates can then be applied to this base template to quickly kickstart a new project.***

