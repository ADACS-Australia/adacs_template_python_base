class Python_package_nameBaseException(Exception):
    """Base class for exceptions raised from {{cookiecutter.__package_name}}"""

    def __init__(self, message: str):
        self._message = message

    def __str__(self) -> str:
        return f"{self._message}"


# my_module Exceptions


class MyModuleProcessLineError(Python_package_nameBaseException):
    """Raised when an attempt is made to process an invalid line"""

    pass


class MyModuleCreateFileError(Python_package_nameBaseException):
    """Raised when a failure is encountered while creating a file"""

    pass


class MyModuleProcessFileError(Python_package_nameBaseException):
    """Raised when a failure is encountered while processing a file"""

    pass
