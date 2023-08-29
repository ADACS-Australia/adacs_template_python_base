# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
SOURCEDIR     = docs
BUILDDIR      = docs/_build

# Set some variables needed by the documentation
PKG_PROJECT := $(shell poetry run python3 -c 'from tomllib import load;print(load(open("pyproject.toml","rb"))["tool"]["poetry"]["name"])')
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

# Documentation targets

clean-docs:
	@rm -rf build docs/_build

content: clean-docs
	@echo "Building documentation for:"
	@echo "   project: "${PKG_PROJECT}
	@echo "   version: "${PKG_VERSION}

docs: content
	@$(SPHINXBUILD) -M html "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
