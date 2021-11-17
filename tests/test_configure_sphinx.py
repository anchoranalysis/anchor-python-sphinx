from unittest import mock
from anchor_python_sphinx import configure


def test_configure():
    """Runs the configure script on a mock, just to make sure no obvious errors occur."""
    mock_sphinx_application = mock.Mock()
    configure(mock_sphinx_application, "2.5")
