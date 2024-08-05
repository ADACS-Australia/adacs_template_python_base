# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
import os
import sys
from tomllib import load


def format_authors(authors):
    if type(authors) is list:
        result = ""
        for i_author, author in enumerate(authors):
            if i_author == 0:
                result = result + f"{author}"
            elif i_author < (len(authors) - 1):
                result = result + f", {author}"
            else:
                result = result + f", and {author}"
    elif type(authors) is str:
        result = authors
    return result


sys.path.insert(0, os.path.abspath("../python"))

# -- Project information -----------------------------------------------------

project = load(open("../pyproject.toml", "rb"))["tool"]["poetry"]["name"]
author = format_authors(
    load(open("../pyproject.toml", "rb"))["tool"]["poetry"]["authors"]
)
copyright_year = 2023
copyright = f"{copyright_year}, {author}"

# These versions are just placeholders.  The point of truth for versions is
# the last tag on the main branch with a "vX.Y.Z*" format.  This can
# be accessed through installed project metadata.

# The short X.Y.Z version
version = "0.0.0"

# The full version, including alpha/beta/rc tags (just a placeholder)
release = "0.0.0-dev"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx.ext.todo",
    "sphinx_click",
    "sphinx.ext.doctest",
    "sphinx.ext.mathjax",
    "sphinx.ext.autosectionlabel",
    "myst_parser",
    "sphinx.ext.todo",
    "sphinx_copybutton",
    "sphinx.ext.napoleon",
]

# Extensions for the Myst-Parser
myst_enable_extensions = [
    "attrs_inline",
    "colon_fence",
    "amsmath",
    "dollarmath",
]

# Set the prompt text that you want the docs copy button to ignore when
# copying code cells
copybutton_prompt_text = "$ "

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

source_suffix = {
    ".rst": "restructuredtext",
    ".txt": "markdown",
    ".md": "markdown",
}

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = "en"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# Sort documented members by the order in which they occur in code
autodoc_member_order = "bysource"

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["assets"]


# -- Extension configuration -------------------------------------------------

# -- Options for todo extension ----------------------------------------------

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True


# Handler for excluding modules, classes, etc from documentation
# Presently, this just passes through the default behavior
def autodoc_skip_member_handler(app, what, name, obj, skip, options):
    # Include everything else
    return skip  # True if you want to exclude; False if you don't


# Automatically called by sphinx at startup
def setup(app):
    # Connect the autodoc-skip-member event from apidoc to the callback
    app.connect("autodoc-skip-member", autodoc_skip_member_handler)
