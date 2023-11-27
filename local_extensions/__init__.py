import datetime
from re import sub
from jinja2.ext import Extension
from jinja2.environment import Environment


class CurrentYearExtension(Extension):
    """Jinja2 extension to return the current year as a string."""

    def __init__(self, environment: Environment):
        """Initialize the extension with the given environment."""
        super().__init__(environment)

        environment.globals.update({"current_year": datetime.datetime.utcnow().year})


class UnderlineExtension(Extension):
    """Jinja2 extension to return an underlined version of a string."""

    def __init__(self, environment: Environment):
        """Initialize the extension with the given environment."""
        super().__init__(environment)

        def underline(s: str, char_ul: str = "-") -> str:
            """Create an underlined version of a string

            Parameters
            ----------
            s : str
                String to underline
            char_ul : str
                Character to underline with (default: '-')

            Returns
            -------
            str
                Underlined string
            """
            return f"{s}\n{char_ul*len(s)}"

        environment.filters.update({"underline": underline})


class PascalCaseExtension(Extension):
    """Jinja2 extension to return a Pascal Case version of a string."""

    def __init__(self, environment: Environment):
        """Initialize the extension with the given environment."""
        super().__init__(environment)

        def pascal_case(s: str) -> str:
            """Create a Pascal Case version of a string

            Parameters
            ----------
            s : str
                String to reformat

            Returns
            -------
            str
                Reformated string
            """
            return "".join(sub(r"(_|-)+", " ", s).title().replace(" ", ""))

        environment.filters.update({"pascal_case": pascal_case})


class EscapeQuotes(Extension):
    """Jinja2 extension to return a version of a string with escape-encoded quotes."""

    def __init__(self, environment: Environment):
        """Initialize the extension with the given environment."""
        super().__init__(environment)

        def escape_quotes(s: str) -> str:
            """Create a version of a string with escape-encoded quotes

            Parameters
            ----------
            s : str
                String to encode

            Returns
            -------
            str
                Encoded string
            """
            return s.replace('"', r"\"")

        environment.filters.update({"escape_quotes": escape_quotes})
