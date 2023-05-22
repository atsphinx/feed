"""Simple RSS feed generator based Open Graph."""
from sphinx.application import Sphinx

__version__ = "0.0.0"


def setup(app: Sphinx):  # noqa: D103
    app.add_config_value(
        "feed_default_summary",
        "Please see content by go to link.",
        "html",
        [str],
    )
    return {
        "version": __version__,
        "env_version": 1,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
