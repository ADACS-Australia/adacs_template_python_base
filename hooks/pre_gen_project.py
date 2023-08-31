import re
import sys


def package_name_check():
    """Check that the cookiecutter package name is valid"""

    MODULE_REGEX = r"^[_a-zA-Z][_a-zA-Z0-9]+$"

    module_name = "{{ cookiecutter.__package_name }}"

    if not re.match(MODULE_REGEX, module_name):
        print(
            f'ERROR: The package name "{module_name}" is not a valid Python module name.'
        )

        sys.exit(1)


if __name__ == "__main__":
    package_name_check()
