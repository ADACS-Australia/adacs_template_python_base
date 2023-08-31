import {{cookiecutter.__package_name}}
import {{cookiecutter.__package_name}}.cli as cli
from click.testing import CliRunner
from pathlib import Path


def test_cli_help(tmp_path: Path) -> None:
    """Make sure that help runs without an error

    Parameters
    ----------
    tmp_path : Path
        Temporary path, generated from a pytest fixture
    """
    runner = CliRunner()
    with runner.isolated_filesystem(temp_dir=tmp_path):
        result = runner.invoke(
            cli.cli,
            [
                "--help",
            ],
        )
        assert result.exit_code == 0


def test_cli_version(tmp_path: Path) -> None:
    """Make sure that version runs without an error and generates the correct result

    Parameters
    ----------
    tmp_path : Path
        Temporary path, generated from a pytest fixture
    """
    runner = CliRunner()
    with runner.isolated_filesystem(temp_dir=tmp_path):
        result = runner.invoke(
            cli.cli,
            [
                "--version",
            ],
        )
        assert result.exit_code == 0
        {% raw %}assert result.output == f"cli, version {{% endraw %}{{cookiecutter.__package_name}}{% raw %}.__version__}\n"{% endraw %}
