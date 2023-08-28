import datetime
from jinja2.ext import Extension
from jinja2.environment import Environment


class CurrentYearExtension(Extension):
    """Jinja2 extension to return the current year as a string."""

    def __init__(self, environment: Environment):
        """Initialize the extension with the given environment."""
        super().__init__(environment)

        environment.globals.update({ "current_year": datetime.datetime.utcnow().year })

class UnderlineExtension(Extension):
    """Jinja2 extension to return an underlined version of a string."""

    def __init__(self, environment: Environment):
        """Initialize the extension with the given environment."""
        super().__init__(environment)

        def underline(s: str, char_ul: str = "-") ->str:
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

        environment.filters.update({'underline': underline})
