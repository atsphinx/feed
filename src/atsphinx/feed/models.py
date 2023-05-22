"""Data-models for feed.

This modue defines brige classes from doctree to feed.

Refs
----

* https://www.rfc-editor.org/rfc/rfc4287
"""
from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional

from atsphinx.og_article.models import og_article
from docutils import nodes
from sphinx.application import Sphinx


@dataclass
class Entry:
    """Data for entry in Atom feed."""

    title: str
    link: str
    updated: datetime
    summary: str


@dataclass
class Feed:
    """Data for Atom feed."""

    title: str
    link: str
    author: str
    entries: List[Entry]

    @property
    def updated(self) -> Optional[datetime]:
        """Value of updated time for feed itself."""
        if not self.entries:
            return None
        return max([e.updated for e in self.entries])

    @classmethod
    def init(cls, app: Sphinx):
        """Create feed object frmo Sphinx application."""
        return cls(
            title=app.config.html_title,
            link=f"{app.config.html_baseurl}/",
            author=app.config.author,
            entries=[],
        )


def generate_entry(app: Sphinx, docname: str) -> Entry:
    """Parse and generate entry object from doctree node."""
    document = app.env.get_doctree(docname)
    if not document:
        raise ValueError(f"Document '{docname}' is not found.")
    article_nodes = list(document.findall(og_article))
    if not article_nodes:
        raise ValueError("This document have og_article node")
    return Entry(
        title=list(document.findall(nodes.title))[0].astext(),
        link=f"{app.config.html_baseurl}/{app.builder.get_target_uri(docname)}",
        updated=article_nodes[0]["modified_time"],
        # TODO: Auto-generate from content
        summary=app.config.feed_default_summary,
    )
