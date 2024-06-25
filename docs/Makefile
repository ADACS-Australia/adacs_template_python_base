# Minimal makefile for Sphinx documentation

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
SOURCEDIR     = docs
BUILDDIR      = docs/_build

# Exclude the following (space-separated) paths from the docs
PATH_EXCLUDE_LIST = docs hooks local_extensions

# Set some variables needed by the documentation
PKG_PROJECT := $(shell poetry run python3 -c 'from tomllib import load;print(load(open("pyproject.toml","rb"))["tool"]["poetry"]["name"])')
PKG_AUTHOR  := $(shell poetry run python3 -c 'from importlib.metadata import metadata; print(metadata("${PKG_PROJECT}")["author"])')
PKG_VERSION := $(word 2,$(shell poetry version))
PKG_RELEASE := ${PKG_VERSION}

# Put help first so that "make" without an argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Project targets

clean: clean-docs
	@rm -rf dist
	@rm -rf .tests
	@rm -rf .pytest_cache
	@rm -rf .cache
	@rm -rf .ropeproject
	@find . -type d -name "__pycache__" -exec rm -rf {} \;
	@find . -type d -name ".mypy_cache" -exec rm -rf {} \;

# Documentation targets

clean-docs:
	@rm -rf build docs/_build

content: clean-docs
	# Make sure this remains, even if it does nothing, because it gets called in .readthedocs.yml

docs: content
	@echo "Building documentation for:"
	@echo "   project: ${PKG_PROJECT}"
	@echo "   author:  ${PKG_AUTHOR}"
	@echo "   version: ${PKG_VERSION}"
	@$(SPHINXBUILD) -M html "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
