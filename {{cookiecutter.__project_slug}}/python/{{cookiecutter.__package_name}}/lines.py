import {{cookiecutter.__package_name}} as pkg
from math import isqrt


class ProcessLineError(pkg.BaseException):
    """Raised when an attempt is made to process an invalid line"""

    pass


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
        raise ProcessLineError(
{% raw %}
            f"Invalid line passed as input: {{{line}}}."
{% endraw %}
        ) from e
