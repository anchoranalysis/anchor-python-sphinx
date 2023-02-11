"""Configures project-related settings."""

import datetime
from typing import Optional

from sphinx import config


def configure_project(
    config: config.Config,
    project_name: str,
    version: Optional[str],
    author: Optional[str],
) -> None:
    """Configures projected-related configuration settings.

    Args:
        config: the configuration.
        project_name: the name of the project, as displayed in the documentation.
        version: an optional version for the documentation.
        author: an optional author for the documentation.
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
