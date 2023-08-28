{{ [cookiecutter.name_package,' CLI Documentation'] | join | underline('=') }}

This package provides a CLI interface through which common tasks can be accomplished.

.. click:: {{ cookiecutter.name_package }}.cli:cli
   :prog: {{ cookiecutter.name_package }}
   :show-nested:
