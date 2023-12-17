import {{cookiecutter.__package_name}} as pkg
import {{cookiecutter.__package_name}}.lines as lines
import os
from pathlib import Path
from typing import List


class CreateFileError(pkg.BaseException):
    """Raised when a failure is encountered while creating a file"""

    pass


class ProcessFileError(pkg.BaseException):
    """Raised when a failure is encountered while processing a file"""

    pass


class ReadFileError(pkg.BaseException):
    """Raised when a failure is encountered while reading a file"""

    pass


def create_file(filename_out: str | Path, n_lines: int = 10) -> None:
    """Create a text file consisting of one +ve integer per line

    Parameters
    ----------
    filename_out : str
        Filename of the file to be written
    n_lines : int
        Optional number of lines to output
    """
    try:
        with open(
            filename_out, "x"
        ) as file:  # 'x' mode is write, but only if file does not exist
            # ======= LOGIC =======
            for i_line in range(n_lines):
                line_i = lines.create_line(i_line)
                file.write(line_i)
            # =====================
    except OSError as e:
        raise CreateFileError(f"Could not open output file {% raw %}{{{filename_out}}}{% endraw %}.") from e
    except (TypeError, ValueError) as e:
        raise CreateFileError("Invalid line generated.") from e


def process_file(filename_in: str | Path, inverse: bool = False) -> None:
    """Process a file

    Parameters
    ----------
    filename_in : str
        The filename of the input file
    inverse : bool
        A boolean flag indicating whether the process action should be inverted
    """
    basename, extension = os.path.splitext(filename_in)
    filename_out = basename + "_modified" + extension

    try:
        with open(filename_in, "r") as file_in, open(filename_out, "w") as file_out:
            try:
                line = file_in.readline()
                while line:
                    line = line.rstrip()
                    output_i = lines.process_line(line, inverse=inverse)
                    file_out.write(f"{output_i}\n")
                    line = file_in.readline()
            except (OSError, lines.ProcessLineError) as e:
                raise ProcessFileError(
                    f"Failed to process file {% raw %}{{{filename_in}}}{% endraw %}."
                ) from e
    except OSError as e:
        raise ProcessFileError(
            f"File open/close error when processing files {% raw %}{{{filename_in}}}{% endraw %}->{% raw %}{{{filename_out}}}{% endraw %}."
        ) from e


def read_file(filename_in: str | Path) -> List[str]:
    """Read a file

    Parameters
    ----------
    filename_in : str
        The filename of the input file
    """
    basename, extension = os.path.splitext(filename_in)

    lines = []
    try:
        with open(filename_in, "r") as file_in:
            line = file_in.readline()
            while line:
                lines.append(line.rstrip())
                line = file_in.readline()
    except OSError as e:
        raise ReadFileError(
            f"File open/close error when reading file {% raw %}{{{filename_in}}}{% endraw %}."
        ) from e

    return lines
