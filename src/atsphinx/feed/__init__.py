"""Simple RSS feed generator based Open Graph."""
from sphinx.application import Sphinx
from sphinx.config import Config

from . import processors

__version__ = "0.1.1"


def validate_config(app: Sphinx, config: Config):
    """Check that other config are exists.

    This extension requires some config values from core or other extension.
    Func raise error if config values are exists.
    """
    if not config.html_baseurl:
        raise ValueError(f"{__name__} require 'html_baseurl' in conf.py")


def setup(app: Sphinx):  # noqa: D103
    app.add_config_value(
        "feed_title",
        None,
        "html",
        [str],
    )
    app.add_config_value(
        "feed_default_summary",
        "Please see content by go to link.",
        "html",
        [str],
    )
    app.add_config_value(
        "feed_out_path",
        "atom.xml",
        "html",
        [str],
    )
    app.connect("config-inited", validate_config)
    app.connect("html-page-context", processors.append_link_for_feed)
    app.connect("build-finished", processors.generate_feed)
    return {
        "version": __version__,
        "env_version": 1,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
