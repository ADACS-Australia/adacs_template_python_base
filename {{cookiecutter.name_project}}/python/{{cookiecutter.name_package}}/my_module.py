import os
from math import isqrt
import {{ cookiecutter.name_package }}.exceptions as ex


def create_line(input: int) -> str:
    """Create a line of output from a +ve integer

    Parameters
    ----------
    input : int
        A +ve integer to turn into a line of output

    Returns
    -------
    str
        A carriage-returned string, to be written to file
    """
{% raw %}
    if not isinstance(input, int):
        raise TypeError(f"A +ve integer is expected as input; received {{{input}}}.")
    if input < 0:
        raise ValueError(f"A +ve integer is expected as input; received {{{input}}}.")
{% endraw %}
    # ======= LOGIC =======
    output = input
    # =====================
    return f"{output}\n"


def process_line(line: str, inverse: bool = False) -> int:
    """Take a sting with a +ve integer and process it

    Parameters
    ----------
    line : str
        A line of text, generally read from a file
    inverse : bool
        A boolean flag indicating whether the process action should be inverted

    Returns
    -------
    int
        A +ve integer, processed from the input line
    """
    try:
        # ======= LOGIC =======
        input = int(line)
        if inverse:
            return isqrt(input)
        else:
            return input * input
        # =====================
    except (ValueError, TypeError) as e:
        raise ex.MyModuleProcessLineError(
{% raw %}
            f"Invalid line passed as input: {{{line}}}."
{% endraw %}
        ) from e


def create_file(filename_out: str, n_lines: int = 10) -> None:
    """Create a text file consisting of one +ve integer per line

    Parameters
    ----------
    filename_out : str
        Filename of the file to be written
    n_lines : int
        Optional number of lines to output
    """
    try:
        with open(filename_out, "w") as file:
            # ======= LOGIC =======
            for i_line in range(n_lines):
                line_i = create_line(i_line)
                file.write(line_i)
            # =====================
    except OSError as e:
        raise ex.MyModuleCreateFileError(
{% raw %}
            f"Could not open output file {{{filename_out}}}."
{% endraw %}
        ) from e
    except (TypeError, ValueError) as e:
        raise ex.MyModuleCreateFileError("Invalid line generated.") from e


def process_file(filename_in: str, inverse: bool = False) -> None:
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
                    output_i = process_line(line, inverse=inverse)
                    file_out.write(f"{output_i}\n")
                    line = file_in.readline()
            except (OSError, ex.MyModuleProcessLineError) as e:
                raise ex.MyModuleProcessFileError(
{% raw %}
                    f"Failed to process file {{{filename_in}}}."
{% endraw %}
                ) from e
    except OSError as e:
        raise ex.MyModuleProcessFileError(
{% raw %}
            f"File open/close error when processing files {{{filename_in}}}->{{{filename_out}}}."
{% endraw %}
        ) from e
