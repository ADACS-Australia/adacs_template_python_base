from {{cookiecutter.name_package}} import my_module
import {{cookiecutter.name_package}}.exceptions as ex
import pytest
import stat
import os
from pathlib import Path
from pytest_mock import MockerFixture

# Invalid inputs to 'create_line' and the exceptions expected
invalid_input = [["string", TypeError], [3.1415, TypeError], [-1, ValueError]]


def create_unwritable_file(
    path: Path, filenamne_base: str = "unwritable_filename"
) -> Path:
    """Create an empty write-protected file

    Parameters
    ----------
    path : Path
        Destination of the output file; usually generated with the tmp_path fixture
    filenamne_base : str
        Filename of the output file

    Returns
    -------
    Path
        Path to the resulting file
    """
    file_path = path / f"{filenamne_base}"
    file = open(file_path, "w")
    file.close()
    os.chmod(file_path, stat.S_IREAD)
    return file_path


def test_my_module_create_file_open_fail(tmp_path: Path) -> None:
    """Verify that the failure to open a file for writing by create_file raises the appropriate exception

    Parameters
    ----------
    tmp_path : Path
        Temporary path, generated from a pytest fixture
    """
    with pytest.raises(ex.MyModuleCreateFileError):
        my_module.create_file(create_unwritable_file(tmp_path))


def test_my_module_create_line_invalid_input() -> None:
    """Verify that invalid inputs generate appropriate exceptions"""
    for input_i, ex_expected in invalid_input:
        with pytest.raises(ex_expected):
            my_module.create_line(input_i)


def test_my_module_create_file_invalid_line(
    tmp_path: Path, mocker: MockerFixture
) -> None:
    """Verify that the the generation of an exception in create_line
    results in the correct exception being created by create_file

    Parameters
    ----------
    tmp_path : Path
        Temporary path, generated from a pytest fixture
    mocker : MockerFixture
        Fixture used to patch create_line
    """
    for ex_expected in [TypeError, ValueError]:
        mocker.patch(
            "{{cookiecutter.name_package}}.my_module.create_line", side_effect=ex_expected
        )
        with pytest.raises(ex.MyModuleCreateFileError):
            my_module.create_file(tmp_path / "test")


def test_my_module_process_file_open_input_file_error(tmp_path: Path) -> None:
    """Verify that an attempt to process a file that does not exist
    raises the correct exception

    Parameters
    ----------
    tmp_path : Path
        Temporary path, generated from a pytest fixture
    """
    file_to_test = tmp_path / "file_that_does_not_exist"
    with pytest.raises(ex.MyModuleProcessFileError):
        my_module.process_file(file_to_test)


def test_my_module_process_file_open_output_file_error(tmp_path: Path) -> None:
    """Verify that the failure to open a file for writing by process_file raises the appropriate exception

    Parameters
    ----------
    tmp_path : Path
        Temporary path, generated from a pytest fixture
    """
    file_input_test = tmp_path / "file_in.txt"
    my_module.create_file(file_input_test)
    create_unwritable_file(tmp_path, "file_in_modified.txt")
    with pytest.raises(ex.MyModuleProcessFileError):
        my_module.process_file(file_input_test)
