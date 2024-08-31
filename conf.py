import time

exclude_patterns = ["README.md"]

extensions = [
    "myst_parser",
    "sphinx_markdown_tables",
    "sphinx_tabs.tabs",
    "sphinxcontrib.httpdomain",
    "sphinxext.opengraph",
    "furo50",
]

html_css_files = [
    "custom.css",
    "announcement.css",
    "https://use.fontawesome.com/releases/v5.13.0/css/all.css",
]
html_js_files = [
    "custom.js",
    "announcement.js",
]
html_static_path = ["_static"]
html_theme = "furo"
html_theme_options = {
    "display_version": False,
    "prev_next_buttons_location": False,
    "sticky_navigation": False,
}
html_title = "CS50 Docs"
html_permalinks_icon = "#"
html_theme_options = {
    "announcement": (
        "This documentation is hosted here only for testing. Please use "
        "<a href='https://cs50.readthedocs.io/'>the main documentation</a> instead."
    )
}

myst_heading_anchors = 6

ogp_image = "https://cs50.readthedocs.io/_images/2ep2od.jpg"
ogp_image_alt = "ALL THE DOCS"
ogp_site_url = "https://cs50.readthedocs.io/"

project = "CS50 Docs"
