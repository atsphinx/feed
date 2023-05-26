"""Integration tests."""
from pathlib import Path

import pytest
from bs4 import BeautifulSoup
from sphinx.testing.util import SphinxTestApp


@pytest.fixture
def outdir(app: SphinxTestApp):
    """Fixture to pass out dir as ``pathlib.Path`` from SphinxTestApp."""
    app.build()
    return Path(app.outdir).resolve()


class TestForBuildReults:
    """Test cases for generated content by build with default settings."""

    def test__generated_xml(self, outdir: Path):  # noqa: D102
        feed_path = outdir / "atom.xml"
        assert feed_path.exists()
        soup = BeautifulSoup(feed_path.read_text(), "xml")
        assert soup.feed.id.text == "http://example.com/"
        assert soup.feed.title.text == "EXAMPLE"
        assert len(soup.find_all("entry")) == 1
        entry = soup.find("entry")
        assert entry.title.text == "Article title"

    def test__index_html(self, outdir: Path):  # noqa: D102
        html_path = outdir / "index.html"
        soup = BeautifulSoup(html_path.read_text(), "lxml")
        assert soup.find_all("link", {"type": "application/atom+xml"})

    def test__article_html(self, outdir: Path):  # noqa: D102
        html_path = outdir / "article.html"
        soup = BeautifulSoup(html_path.read_text(), "lxml")
        assert soup.find_all("link", {"type": "application/atom+xml"})
