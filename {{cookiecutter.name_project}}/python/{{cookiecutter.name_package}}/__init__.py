from importlib import metadata  # make sure to import metadata explicitly

__version__ = metadata.version(__package__ or __name__)
