"""Standard tests."""
from io import StringIO
from pathlib import Path

import pytest
from sphinx.errors import ExtensionError
from sphinx.testing.util import SphinxTestApp

from atsphinx.feed import models


@pytest.mark.sphinx("html")
def test__it(app: SphinxTestApp, status: StringIO, warning: StringIO):
    """Test to pass."""


class TestFor_generate_entry:  # noqa: D101
    @pytest.mark.sphinx("html")
    def test_default(self, app: SphinxTestApp, status: StringIO, warning: StringIO):
        """Simple test for generating entry object."""
        app.builder.read_doc("article")
        entry = models.generate_entry(app, "article")
        assert entry.title == "Article title"
        assert entry.updated.strftime("%Y-%m-%d") == "2023-01-01"
        assert entry.link == "http://example.com/article.html"
        assert entry.summary == "Please see content by go to link."

    @pytest.mark.sphinx(
        "html",
        confoverrides={
            "feed_default_summary": "test description",
        },
    )
    def test_configured_summary(
        self, app: SphinxTestApp, status: StringIO, warning: StringIO
    ):
        """Simple test for generating entry object."""
        app.builder.read_doc("article")
        entry = models.generate_entry(app, "article")
        assert entry.summary == "test description"


class TestFor_generate_feed:  # noqa: D101
    @pytest.mark.sphinx("html")
    def test_default(self, app: SphinxTestApp, status: StringIO, warning: StringIO):
        """Single test for generate feeed object."""
        feed = models.Feed.init(app)
        assert feed.title == "EXAMPLE"
        assert feed.link == "http://example.com/"
        assert feed.author == "Tester"

    @pytest.mark.sphinx(
        "html",
        confoverrides={
            "feed_title": "test title",
        },
    )
    def test_configured_title(
        self, app: SphinxTestApp, status: StringIO, warning: StringIO
    ):
        """Simple test for generating entry object."""
        feed = models.Feed.init(app)
        assert feed.title == "test title"


class TestFor_sphinx_config:  # noqa: D101
    @pytest.mark.sphinx("html", testroot="no_html_baseurl")
    def test_raise__no_html_baseurl(self, app_params, make_app):
        """Raises error when create Sphinx app that do not have html_baseurl in conf."""
        with pytest.raises(ExtensionError):
            args, kwargs = app_params
            make_app(*args, **kwargs)


class TestFor_build_fed:  # noqa: D101
    @pytest.mark.sphinx("html")
    def test_default(self, app: SphinxTestApp):
        """Raises error when create Sphinx app that do not have html_baseurl in conf."""
        app.build()
        assert (Path(app.outdir) / "atom.xml").exists()
