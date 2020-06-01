extensions = [
    "recommonmark",
    #"sphinx.ext.autodoc",
    #"sphinx_markdown_tables"
]

html_static_path = ["_static"]

html_css_files = ["css/custom.css"]
html_theme = "sphinx_rtd_theme"
html_theme_options = {
    "prev_next_buttons_location": False,
    "sticky_navigation": False
}
html_title = "CS50 Docs"

master_doc = "index"

project = "CS50 Docs"
