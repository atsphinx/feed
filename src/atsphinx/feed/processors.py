# noqa: D100
# TODO: Write after
from pathlib import Path
from typing import Optional
from xml.etree import ElementTree as ET

from feedgen.feed import FeedGenerator
from sphinx import addnodes
from sphinx.application import Sphinx

from . import models


def generate_feed(app: Sphinx, exc: Exception):
    """Generate feed file content into outdir."""
    feed = models.Feed.init(app)
    for docname in app.env.all_docs.keys():
        try:
            feed.entries.append(models.generate_entry(app, docname))
        except ValueError:
            continue
    fg = FeedGenerator()
    fg.id(feed.link)
    fg.title(feed.title)
    fg.link(href=feed.link, rel="alternate")
    for entry in feed.entries:
        print(entry.link)
        fg_entry = fg.add_entry()
        fg_entry.id(entry.link)
        fg_entry.link(href=entry.link)
        fg_entry.title(entry.title)
        fg_entry.summary(entry.summary)
    out_path = Path(app.outdir) / app.config.feed_out_path
    fg.atom_file(out_path)


def append_link_for_feed(
    app: Sphinx,
    pathname: str,
    templatename: str,
    context: dict,
    doctree: Optional[addnodes.document] = None,
):
    """Pick og attributes from document and inject into metatags."""
    feed = models.Feed.init(app)
    elm = ET.Element(
        "link",
        {
            "rel": "alternate",
            "type": "application/atom+xml",
            "href": feed.link,
        },
    )
    if "metatags" not in context:
        context["metatags"] = ""
    context["metatags"] += f"\n{ET.tostring(elm).decode()}"
