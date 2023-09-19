import subprocess

# Rich is a cookiecutter dependency, so these should be safe here
from rich.console import Console
from rich.markdown import Markdown


def git():
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


def venv():
    pass
    # Check if PYENV_VERSION is defined and if so, that it's set to system?
    # subprocess.call(["poetry", "config", "--local", "virtualenvs.in-project", "true"])
    # subprocess.call(["poetry", "config", "--local", "virtualenvs.create", "true"])


def install():
    pass
    # subprocess.call(["poetry","install","--all-extras"])


def print_instructions():

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
    venv()
    install()
    print_instructions()
