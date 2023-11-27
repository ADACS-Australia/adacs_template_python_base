import subprocess

# Rich is a cookiecutter dependency, so these should be safe here
from rich.console import Console
from rich.markdown import Markdown


def git() -> None:
    """Create and configure a git repo for the rendered project"""
    subprocess.call(["git", "init"])
    subprocess.call(["git", "add", "*"])
    subprocess.call(
        [
            "git",
            "remote",
            "add",
            "origin",
            "https://github.com/{{cookiecutter.github_login}}/{{cookiecutter.__project_slug}}.git",
        ]
    )
    subprocess.call(["git", "commit", "-m", "Initial commit of template code"])
    subprocess.call(["git", "tag", "v0.0.0"])


def venv(venv_type: str) -> None:
    """Create a virtual environment for the rendered project

    Parameters
    ----------
    venv_type : str
        String specifying how the virtual environment is being supported
    """
    if venv_type == "venv":
        # Check if PYENV_VERSION is defined and if so, that it's set to system?
        # raise NotImplementedError()
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
        # raise NotImplementedError()
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
    venv("{{ cookiecutter.virtual_environment }}")
    install("{{ cookiecutter.virtual_environment }}")
    print_instructions()
