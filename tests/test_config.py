"""Test cases for configuration patterns."""
import pytest
from sphinx.errors import ExtensionError


@pytest.mark.sphinx("html", testroot="no_html_baseurl")
def test__fail_by_missing_config(app_params, make_app):
    """Raises error when create Sphinx app that do not have html_baseurl in conf."""
    with pytest.raises(ExtensionError):
        args, kwargs = app_params
        make_app(*args, **kwargs)
