import time

extensions = [
    "recommonmark",
    "sphinx_markdown_tables",
    "sphinx_tabs.tabs",
    "sphinxcontrib.httpdomain",
    "sphinxext.opengraph"
]

html_css_files = [
    "https://cs50.readthedocs.io/_static/custom.css?" + str(round(time.time())),
    "https://use.fontawesome.com/releases/v5.13.0/css/all.css"]
html_js_files = ["https://cs50.readthedocs.io/_static/custom.js?" + str(round(time.time()))]
html_theme = "sphinx_rtd_theme"
html_theme_options = {
    "display_version": False,
    "prev_next_buttons_location": False,
    "sticky_navigation": False
}
html_title = "CS50 Docs"

ogp_image = "https://cs50.readthedocs.io/_images/2ep2od.jpg"
ogp_image_alt = "ALL THE DOCS"
ogp_site_url = "https://cs50.readthedocs.io/"

project = "CS50 Docs"
