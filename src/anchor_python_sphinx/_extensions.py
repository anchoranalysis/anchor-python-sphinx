"""Sets up and configures Sphinx extensions."""

import sphinx
from sphinx import config
from ._auto_api import configure_auto_api
from typing import List


_HTML_STATIC_PATH: str = "_static"
"""The directory (relative-path) where additional stylesheets and other HTML artifacts may be placed."""


_CUSTOM_CSS_NAME: str = "custom.css"
"""The name of the custom.css file (in the above subdirectory) that can further change the CSS."""


_EXTENSIONS: List[str] = [
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx.ext.todo",
    "sphinx.ext.intersphinx",
    "autoapi.extension",
    "sphinx_rtd_theme",
]
"""The names of the extensions that are setup."""


def setup_and_configure_extensions(app: sphinx.application.Sphinx) -> None:
    """Sets up all Sphinx extensions, and perform any additionally needed configuration.

    :param app: the Sphinx application to configure.
    """
    for extension in _EXTENSIONS:
        app.setup_extension(extension)

    configure_auto_api(app)

    _configure_theme(app.config)
    _configure_todo(app.config)
    _configure_intersphinx(app.config)


def _configure_theme(config: config.Config) -> None:
    """Configures which theme is used and additional settings for the theme."""

    config.html_theme = "sphinx_rtd_theme"

    # Add any paths that contain custom static files (such as style sheets) here,
    # relative to this directory. They are copied after the builtin static files,
    # so a file named "default.css" will overwrite the builtin "default.css".
    config.html_static_path = [_HTML_STATIC_PATH]

    # This allows a custom.css change properties of theme (e.g. making the effective page-width wider)
    config.html_css_files = [
        _CUSTOM_CSS_NAME,
    ]


def _configure_todo(config: config.Config) -> None:
    """Configures the todo plugin."""
    # If true, `todo` and `todoList` produce output, else they produce nothing.
    config.todo_include_todos = True


def _configure_intersphinx(config: config.Config) -> None:
    """Configures the intersphinx plugin."""
    config.intersphinx_mapping = {
        "python": ("https://docs.python.org/3", None),
        "pandas": ("http://pandas.pydata.org/pandas-docs/dev", None),
        "numpy": ("https://numpy.org/doc/stable/", None),
        "matplotlib": ("https://matplotlib.org", None),
        "plotly": ("https://plotly.com/python-api-reference/", None),
    }
