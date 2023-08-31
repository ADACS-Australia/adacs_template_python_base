{{ [cookiecutter.__package_name,' CLI Documentation'] | join | underline('=') }}

This package provides a CLI interface through which common tasks can be accomplished.

.. click:: {{ cookiecutter.__package_name }}.cli:cli
   :prog: {{ cookiecutter.__package_name }}
   :show-nested:
