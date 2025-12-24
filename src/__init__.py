from pathlib import Path
import logging

"""Promodoro package initialization.

Expose package metadata and a package logger.
"""
# Try to read installed package metadata (works when package is installed).
# Try to read installed package metadata (works when package is installed).
try:
    from importlib.metadata import version, metadata, PackageNotFoundError
except Exception:
    # Fallback for older Python (if importlib_metadata is available).
    try:
        from importlib_metadata import version, metadata, PackageNotFoundError  # type: ignore
    except Exception:
        version = lambda name: "0.0.0"  # type: ignore
        metadata = lambda name: {}  # type: ignore
        PackageNotFoundError = Exception  # type: ignore
_pkg_name = Path(__file__).parent.name

try:
    __version__ = version(_pkg_name)
except PackageNotFoundError:
    __version__ = "0.0.0"

try:
    _meta = metadata(_pkg_name) or {}
    __author__ = _meta.get("Author", "") or _meta.get("Author-email", "")
    __license__ = _meta.get("License", "")
except Exception:
    __author__ = ""
    __license__ = ""

# Package logger (library should attach handlers as needed).
logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

def get_version():
    """Return the package version string."""
    return __version__

__all__ = ["__version__", "__author__", "__license__", "get_version", "logger"]