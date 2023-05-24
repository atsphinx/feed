# noqa: D100
# TODO: Write after
from pathlib import Path

from feedgen.feed import FeedGenerator
from sphinx.application import Sphinx

from . import models


def generate_feed(app: Sphinx, exc: Exception):
    """Generate feed file content into outdir."""
    feed = models.Feed.init(app)
    fg = FeedGenerator()
    fg.id(feed.link)
    fg.title(feed.title)
    out_path = Path(app.outdir) / app.config.feed_out_path
    fg.atom_file(out_path)
