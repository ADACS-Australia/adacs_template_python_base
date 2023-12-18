import subprocess

# Rich is a cookiecutter dependency, so these should be safe here
from rich.console import Console
from rich.markdown import Markdown


def git() -> None:
    """Create and configure a git repo for the rendered project"""
    result = subprocess.run(["git", "init", "-b", "main"])
    result = subprocess.run(["git", "config",  "--local", "push.followTags", "true" ])
    result = subprocess.run(["git", "config",  "--local", "--add", "remote.origin.tagopt", "--tags" ])
    result = subprocess.run(
        [
            "git",
            "remote",
            "remove",
            "origin"
        ]
    )
    result = subprocess.run(
        [
            "git",
            "remote",
            "add",
            "origin",
            "git@github.com:{{cookiecutter.github_login}}/{{cookiecutter.github_repo}}.git"
        ]
    )
    # This is needed to make sure that the committed poetry.lock file is up-to-date
    result = subprocess.run(["poetry", "update"])
    result = subprocess.run(["git", "add", "*"])
    result = subprocess.run(["git", "commit", "-m", "Initial commit of template code"])
    # Make sure this is an annotated tag or it won't be pushed to remote and the version
    # management won't be initialised correctly
    result = subprocess.run(["git", "tag", "-a", "v0.0.0", "-m", "Initialised with template"])


def venv(venv_type: str) -> None:
    """Create a virtual environment for the rendered project.  IMPLEMENTATION UNFINISHED.

    When this has been implemented properly, add the following to the cookiecutter.json file:

    {% raw %}
    ================================================================
    "virtual_environment": ["venv","pyenv","poetry","conda","none"],
    ...
    "__prompts__": {
        "virtual_environment":{
            "__prompt__": "How will you manage your virtual env?:",
            "venv":   "Virtualenv",
            "pyenv":  "pyenv-virtualenv",
            "poetry": "Poetry",
            "conda":  "Conda",
            "none":   "I'll set this up myself."
        }
    }
    ================================================================
    {% endraw %}

    Parameters
    ----------
    venv_type : str
        String specifying how the virtual environment is being supported
    """
    raise NotImplementedError()
    if venv_type == "venv":
        # Check if PYENV_VERSION is defined and if so, that it's set to system?
        pass
    elif venv_type == "poetry":
        # Check if PYENV_VERSION is defined and if so, that it's set to system?
        # result = subprocess.run(["poetry", "config", "--local", "virtualenvs.in-project", "true"])
        # result = subprocess.run(["poetry", "config", "--local", "virtualenvs.create",     "true"])
        pass
    elif venv_type == "pyenv":
        # result = subprocess.run(["pyenv", "virtualenv", "3.11", "{{cookiecutter.__project_slug}}"])
        # result = subprocess.run(["pyenv", "local", "{{cookiecutter.__project_slug}}"])
        pass
    elif venv_type == "Conda":
        pass
    elif venv_type == "none":
        pass
    else:
        raise ValueError(f"Invalid venv implementation selection given: {venv_type}")


def install(venv_type: str) -> None:
    """Install the rendered project into its virtual environment

    Parameters
    ----------
    venv_type : str
        String specifying how the virtual environment is being supported
    """
    if venv_type in ["venv", "poetry", "pyenv"]:
        result = subprocess.run(["poetry", "install", "--all-extras"])
    elif venv_type == "none":
        pass
    else:
        raise ValueError(f"Invalid venv implementation selection given: {venv_type}")


def print_instructions() -> None:

    """Print instructions about how to configure the rendered project for use"""
    # Read the instructions file, ignoring lines that start with '***'
    with open("INSTRUCTIONS.template", "r") as file:

        # Add a notification that the rendering is complete to the instructions being written
        lines = "# Rendering Complete"

        line_in = file.readline()
        while line_in:
            if line_in[0:2] != "//":
                lines = lines + line_in
            line_in = file.readline()

    # Render the file as Markdown with Rich
    console = Console()
    console.print(Markdown(lines))


if __name__ == "__main__":
    git()
    {% raw %}
    # venv("{{ cookiecutter.virtual_environment }}")
    # install("{{ cookiecutter.virtual_environment }}")
    {% endraw %}
    install("poetry")
    print_instructions()
