"""Test cases for models module."""
import pytest
from sphinx.testing.util import SphinxTestApp

from atsphinx.feed import models


class TestFor_generate_entry:  # noqa: D101
    @pytest.mark.sphinx("html")
    def test_default(self, app: SphinxTestApp):
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
    def test_configured_summary(self, app: SphinxTestApp):
        """Simple test for generating entry object."""
        app.builder.read_doc("article")
        entry = models.generate_entry(app, "article")
        assert entry.summary == "test description"


class TestFor_generate_feed:  # noqa: D101
    @pytest.mark.sphinx("html")
    def test_default(self, app: SphinxTestApp):
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
    def test_configured_title(self, app: SphinxTestApp):
        """Simple test for generating entry object."""
        feed = models.Feed.init(app)
        assert feed.title == "test title"
