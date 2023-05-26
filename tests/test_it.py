"""Standard tests."""
from io import StringIO
from pathlib import Path

import pytest
from bs4 import BeautifulSoup
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
        feed_path = Path(app.outdir) / "atom.xml"
        assert feed_path.exists()
        soup = BeautifulSoup(feed_path.read_text(), "xml")
        assert soup.feed.id.text == "http://example.com/"
        assert soup.feed.title.text == "EXAMPLE"
        assert len(soup.find_all("entry")) == 1
        entry = soup.find("entry")
        assert entry.title.text == "Article title"

    @pytest.mark.sphinx("html")
    def test_html(self, app: SphinxTestApp):
        """Raises error when create Sphinx app that do not have html_baseurl in conf."""
        app.build()
        html_path = Path(app.outdir) / "index.html"
        soup = BeautifulSoup(html_path.read_text(), "lxml")
        assert soup.find_all("link", {"type": "application/atom+xml"})
