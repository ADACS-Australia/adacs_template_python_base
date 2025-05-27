from contextlib import contextmanager
import shlex
import os
import subprocess
from pathlib import Path
from cookiecutter.utils import rmtree
from pytest_cookies.plugin import Cookies, Result


@contextmanager
def inside_dir(path: Path):
    """
    Execute code from inside the given directory
    :param path: String, path of the directory the command is being run.
    """
    old_path = os.getcwd()
    try:
        os.chdir(path)
        yield
    finally:
        os.chdir(old_path)


@contextmanager
def bake_in_temp_dir(cookies: Cookies, *args, **kwargs):
    """
    Delete the temporal directory that is created when executing the tests
    :param cookies: pytest_cookies.Cookies,
        cookie to be baked and its temporal files will be removed
    """
    result = cookies.bake(*args, **kwargs)
    if not result.project_path:
        raise OSError("Could not bake project.")
    try:
        yield result
    finally:
        rmtree(str(result.project_path))


def run_inside_venv(command, venv_path):
    activate_script = os.path.join(
        venv_path, "venv", "bin", "activate"
    )  # For Linux/macOS

    if os.name == "nt":  # Windows
        process = subprocess.Popen(
            [f"{activate_script} && {command}"],
            shell=True,
            executable=os.environ["COMSPEC"],
        )
    else:  # macOS and Linux
        process = subprocess.Popen(
            [f"source {activate_script} && {command}"],
            shell=True,
            executable="/bin/bash",
        )
    process.wait()

    return process.returncode


def run_inside_dir(command: str, path: Path, source_env=True):
    """
    Run a command from inside a given directory, returning the exit status
    :param command: Command that will be executed
    :param path: String, path of the directory the command is being run.
    """
    with inside_dir(path):
        if source_env:
            result = run_inside_venv(command, path)
        else:
            result = subprocess.check_call(shlex.split(command))
        return result == 0


def source_inside_dir(command: str, path: Path):
    """
    Source a shell script from inside a given directory, returning the exit status
    :param command: Script that will be sourced
    :param path: String, path of the directory the command is being run.
    """
    with inside_dir(path):
        result = subprocess.check_call(shlex.split(command))
        return result


def check_output_inside_dir(command: str, path: Path):
    "Run a command from inside a given directory, returning the command output"
    with inside_dir(path):
        return subprocess.check_output(shlex.split(command))


def project_info(result: Result):
    """Get toplevel dir, project_slug, and project dir from baked cookies"""
    project_slug = result.project_path.name
    project_dir = result.project_path / project_slug
    return str(result.project_path), str(project_slug), str(project_dir)
