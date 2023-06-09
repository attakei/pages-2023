"""Configuration of Sphinx."""
import os
from pathlib import Path

here = Path(__file__).parent
root = here.parent

# -- Project information
project = "attakei pages"
copyright = "2012-2023, Kazuya Takei"
author = "Kazuya Takei"
release = "2023.5.1"

# -- General configuration
extensions = [
    "atsphinx.footnotes",
    "extensions.article_og_image",
    "extensions.rebuild_pageurl",
    "oembedpy.ext.sphinx",
    "sphinxext.opengraph",
]
templates_path = ["_templates"]
exclude_patterns = []
language = "ja"

# -- Options for HTML output
html_theme = "piccolo_theme"
html_title = "attakei pages"
html_baseurl = "https://attakei.net"  # Not need to change by environment
html_static_path = ["_static"]
html_css_files = ["css/site.css"]

# -- Options for Linkcheck builder
linkcheck_allowed_redirects = {
    r"https://sphinx-revealjs\.readthedocs\.io/.*": r"https://sphinx-revealjs\.readthedocs\.io/en/stable/.*",  # noqa: E501
}

# -- Options for extensions
# sphinxext-opengraph
ogp_site_url = html_baseurl
ogp_description_length = 100
ogp_type = "article"
ogp_image = "/_static/og-images/default.png"

# sphinxcontrib-gtagjs (for environment)
if "SITE_GTAGJS_IDS" in os.environ:
    extensions += [
        "sphinxcontrib.gtagjs",
    ]
    gtagjs_ids = os.environ["SITE_GTAGJS_IDS"].split(",")

# extensions.article_og_image
x_aoi_basepath = "_static/og-images"
x_aoi_image_spec = root / "resources" / "og-image_spec-article.toml"
x_aoi_excludes = ["index", "404"]
