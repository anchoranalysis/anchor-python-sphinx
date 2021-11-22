"""Configures project-related settings."""

from sphinx import config
from typing import Optional
import datetime


def configure_project(
    config: config.Config,
    project_name: str,
    version: Optional[str],
    author: Optional[str],
) -> None:
    """Configures projected-related configuration settings.

    :param config: the configuration.
    :param project_name: the name of the project, as displayed in the documentation.
    :param version: an optional version for the documentation.
    :param author: an optional author for the documentation.
    """
    config.project = project_name
    year = datetime.datetime.now().year
    if author is not None:
        config.copyright = f"{year}, {author}"
        config.author = author

    _configure_version(config, version)


def _configure_version(config: config.Config, version: Optional[str]) -> None:
    """Assigns a version if it is specified."""
    if version is not None:
        # The short X.Y version
        config.version = version
        # The full version, including alpha/beta/rc tags
        config.release = version
