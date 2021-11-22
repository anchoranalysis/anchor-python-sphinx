"""Configures the Sphinx AutoAPI plugin."""

from sphinx import application
import re
from typing import Optional, Any


def configure_auto_api(app: application.Sphinx) -> None:
    """Configures the AutoAPI plugin.

    :param app: the Sphinx application to configure.
    """
    app.config.autoapi_type = "python"
    app.config.autoapi_dirs = ["../src"]
    app.config.autoapi_options = [
        "members",
        "undoc-members",
        "show-inheritance",
        "show-module-summary",
        "imported-members",
    ]
    app.config.autoapi_ignore = ["*docs/*", "*test/*", "build/*"]
    app.config.autoapi_add_toctree_entry = True

    _configure_autoapi_skip(app, True, True)


def _configure_autoapi_skip(
    app: application.Sphinx, skip_private: bool, skip_submodules: bool
) -> None:
    """Configures the autoapi on what entities to skip (or not skip) when making the API documentation.

    :param app: the Sphinx application to configure.
    :param skip_private: if True, private attributes, methods etc. are skipped.
    :param skip_submodules: if True, submodules (any module containing a period) are skipped.
    """

    def determine_whether_to_skip(
        app: application.Sphinx,
        what: str,
        name: str,
        obj: Any,
        skip: bool,
        options,
    ) -> Optional[bool]:
        """Exclude all private attributes, methods, and dunder methods from Sphinx."""

        # Maybe skip submodules
        if skip_submodules and what == "module" and ("." in str(obj)):
            return True

        # Maybe skip private attributes, methods etc.
        if skip_private:
            exclude = re.findall(r"\._.*", str(obj))
            return skip or exclude
        else:
            return None

    app.connect("autoapi-skip-member", determine_whether_to_skip)
