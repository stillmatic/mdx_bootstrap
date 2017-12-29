"""The init file."""
from .mdx_bootstrap import BootstrapExtension

__version__ = '1.0.0'


def makeExtension(**kwargs):
    """Register extension."""
    return BootstrapExtension(**kwargs)
