"""Python library for working with command-line editors (like vim)."""

import logging as _logging

from ._vim import vim


__all__ = ["vim"]

__author__ = "Bryan M Bugyi"
__email__ = "bryanbugyi34@gmail.com"
__version__ = "0.1.2"

_logging.getLogger(__name__).addHandler(_logging.NullHandler())
