"""Standard tests."""
from io import StringIO

import pytest
from sphinx.testing.util import SphinxTestApp

from atsphinx.feed import models


@pytest.mark.sphinx("html")
def test__it(app: SphinxTestApp, status: StringIO, warning: StringIO):
    """Test to pass."""


@pytest.mark.sphinx("html")
def test__generate_entry(app: SphinxTestApp, status: StringIO, warning: StringIO):
    """Simple test for generating entry object."""
    app.builder.read_doc("article")
    entry = models.generate_entry(app, "article")
    assert entry.title == "Article title"
    assert entry.updated.strftime("%Y-%m-%d") == "2023-01-01"
    assert entry.link == "http://example.com/article.html"


@pytest.mark.sphinx("html")
def test__generate_feed(app: SphinxTestApp, status: StringIO, warning: StringIO):
    """Single test for generate feeed object."""
    feed = models.Feed.init(app)
    assert feed.title == "EXAMPLE"
    assert feed.link == "http://example.com/"
    assert feed.author == "Tester"
