# noqa: D100
from atsphinx.feed import __version__

# -- Project information
project = "atsphinx-feed"
copyright = "2023, Kazuya Takei"
author = "Kazuya Takei"
release = __version__

# -- General configuration
extensions = [
    "rst_pypi_ref.sphinx",
    "sphinx.ext.todo",
]
templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output
html_theme = "alabaster"
html_static_path = ["_static"]
