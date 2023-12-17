import subprocess

# Rich is a cookiecutter dependency, so these should be safe here
from rich.console import Console
from rich.markdown import Markdown


def git() -> None:
    """Create and configure a git repo for the rendered project"""
    subprocess.call(["git", "init", "-b", "main"])
    subprocess.call(["git", "config",  "--local", "push.followTags", "true" ])
    subprocess.call(["git", "config",  "--local", "remote.origin.tagopt", "--tags" ])
    subprocess.call(["git", "add", "*"])
    subprocess.call(
        [
            "git",
            "remote",
            "add",
            "origin",
            "git@github.com:{{cookiecutter.github_login}}/{{cookiecutter.github_repo}}.git"
        ]
    )
    subprocess.call(["git", "add", "*"])
    subprocess.call(["git", "commit", "-m", "Initial commit of template code"])
    subprocess.call(["git", "tag", "v0.0.0"])


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
        # subprocess.call(["poetry", "config", "--local", "virtualenvs.in-project", "true"])
        # subprocess.call(["poetry", "config", "--local", "virtualenvs.create",     "true"])
        pass
    elif venv_type == "pyenv":
        # subprocess.call(["pyenv", "virtualenv", "3.11", "{{cookiecutter.__project_slug}}"])
        # subprocess.call(["pyenv", "local", "{{cookiecutter.__project_slug}}"])
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
        subprocess.call(["poetry", "install", "--all-extras"])
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
