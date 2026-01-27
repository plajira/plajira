"""plajira: Sync your .plan file with Jira Cloud."""
from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("plajira")
except PackageNotFoundError:
    __version__ = "dev"
