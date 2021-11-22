__author__ = "Owen Feehan"
__copyright__ = "Owen Feehan"
__license__ = "MIT"

from typing import Optional
import sphinx
from ._project import configure_project
from ._scaffolding import configure_general_scaffolding
from ._extensions import setup_and_configure_extensions


def configure(
    app: sphinx.application.Sphinx,
    project_name: str,
    version: Optional[str] = None,
    author: Optional[str] = None,
) -> None:
    """Applies the desired configuration, including plugins, to a Sphinx application.

    :param app: the Sphinx application to configure.
    :param project_name: the name of the project, as displayed in the documentation.
    :param version: an optional version for the documentation.
    :param author: an optional author for the documentation.
    """
    configure_project(app.config, project_name, version, author)

    configure_general_scaffolding(app.config)
    setup_and_configure_extensions(app)
