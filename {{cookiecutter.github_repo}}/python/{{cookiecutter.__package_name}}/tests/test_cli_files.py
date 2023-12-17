import {{cookiecutter.__package_name}}.cli as cli
import {{cookiecutter.__package_name}}.files as files
import filecmp
from os.path import isfile
from click.testing import CliRunner
from pathlib import Path


def test_cli_create_invalid_file(tmp_path: Path) -> None:
    """Check that the correct exception results when a file fails to be created.

    Parameters
    ----------
    tmp_path : Path
        Temporary path, generated from a pytest fixture
    """
    runner = CliRunner()
    basename = "test_cli_process_invalid_file"
    with runner.isolated_filesystem(temp_dir=tmp_path):

        with open(f"{basename}.txt", "w") as file_out:
            file_out.write("1\n2\n3\nA\n")

        result = runner.invoke(
            cli.cli,
            [
                "create-file",
                f"{basename}.txt",
            ],
        )
        assert result.exit_code != 0
        assert isinstance(result.exception, files.CreateFileError)


def test_cli_process_invalid_file(tmp_path: Path) -> None:
    """Check that the correct exception results when an invalid filename is given to 'process'

    Parameters
    ----------
    tmp_path : Path
        Temporary path, generated from a pytest fixture
    """
    runner = CliRunner()
    basename = "test_cli_process_invalid_file"
    with runner.isolated_filesystem(temp_dir=tmp_path):

        with open(f"{basename}.txt", "w") as file_out:
            file_out.write("1\n2\n3\nA\n")

        result = runner.invoke(
            cli.cli,
            [
                "process-file",
                f"{basename}.txt",
            ],
        )
        assert result.exit_code != 0
        assert isinstance(result.exception, files.ProcessFileError)


def test_cli_create_file_n_lines_option(tmp_path: Path) -> None:
    """Check that the '--n_lines' option runs and results in the correct number of lines

    Parameters
    ----------
    tmp_path : Path
        Temporary path, generated from a pytest fixture
    """
    runner = CliRunner()

    n_lines_check = [0, 1, 101]

    with runner.isolated_filesystem(temp_dir=tmp_path):
        for n_lines in n_lines_check:
            basename = f"test_cli_create_file_n_lines_option_{n_lines}"
            result = runner.invoke(
                cli.cli,
                [
                    "create-file",
                    f"--n_lines={n_lines}",
                    f"{basename}.txt",
                ],
            )
            assert result.exit_code == 0
            assert isfile(f"{basename}.txt")

            with open(f"{basename}.txt", "r") as fp:
                count = 0
                for line in fp:
                    count = count + 1
                assert count == n_lines


def test_cli_end_to_end(tmp_path: Path) -> None:
    """Run all the commands end-to-end and check the resulting output

    Parameters
    ----------
    tmp_path : Path
        Temporary path, generated from a pytest fixture
    """
    runner = CliRunner()
    basename = "test_cli_end_to_end_basename"
    with runner.isolated_filesystem(temp_dir=tmp_path):

        result = runner.invoke(
            cli.cli,
            [
                "create-file",
                f"{basename}.txt",
            ],
        )
        assert result.exit_code == 0
        assert isfile(f"{basename}.txt")

        result = runner.invoke(
            cli.cli,
            [
                "process-file",
                f"{basename}.txt",
            ],
        )
        assert result.exit_code == 0
        assert isfile(f"{basename}_modified.txt")

        result = runner.invoke(
            cli.cli,
            [
                "process-file",
                "--inverse",
                f"{basename}_modified.txt",
            ],
        )
        assert result.exit_code == 0
        assert isfile(f"{basename}_modified_modified.txt")
        assert filecmp.cmp(f"{basename}.txt", f"{basename}_modified_modified.txt")
