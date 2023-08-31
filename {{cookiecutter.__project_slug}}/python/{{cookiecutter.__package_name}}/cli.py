import click

import importlib.metadata
import collections

import {{cookiecutter.__package_name}}.my_module as my_module
import {{cookiecutter.__package_name}}.exceptions as ex


CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])
FLEX_CONTEXT_SETTINGS = dict(
    help_option_names=["-h", "--help"],
    ignore_unknown_options=True,
    allow_extra_args=True,  # needed for the passing of model parameters
)


class _OrderedGroup(click.Group):
    """This class is used to ensure that the ordering of the CLI subcommands are in code-order in the CLI help and documentation."""

    def __init__(self, name=None, commands=None, **attrs):
        super(_OrderedGroup, self).__init__(name, commands, **attrs)
        #: the registered subcommands by their exported names.
        self.commands = commands or collections.OrderedDict()
        """An ordered dict of the registered commands"""

    def list_commands(self, ctx: click.core.Context):
        return self.commands


@click.group(cls=_OrderedGroup, context_settings=CONTEXT_SETTINGS)
@click.version_option(importlib.metadata.version("{{cookiecutter.__package_name}}"))
@click.pass_context
def cli(ctx: click.core.Context) -> None:
    """Run code from the {{cookiecutter.__package_name}} package.

    Please see the documentation at https://{{cookiecutter.rtd_project_name}}.readthedocs.io for information about how to work with {{cookiecutter.__package_name | capitalize}}.
    """

    # ensure that ctx.obj exists and is a dict (in case `cli()` is called
    # by means other than the `if` block below)
    ctx.ensure_object(dict)


@cli.command(context_settings=CONTEXT_SETTINGS)
@click.option(
    "--n_lines",
    "-n",
    type=int,
    default=10,
    help="Number of lines to write to the file",
)
@click.argument("filename", type=str)
def create_file(filename: str, n_lines: int) -> None:
    """Create a file"""

    my_module.create_file(filename, n_lines=n_lines)


@cli.command(context_settings=CONTEXT_SETTINGS)
@click.argument("filename", type=click.Path(exists=True))
@click.option(
    "--inverse",
    "-i",
    is_flag=True,
    show_default=True,
    help="Do the inverse of the process-file operation.",
)
def process_file(filename: str, inverse: bool) -> None:
    """Process a file"""

    try:
        my_module.process_file(filename, inverse=inverse)
    except ex.MyModuleProcessFileError as e:
        print(e)
        raise e
