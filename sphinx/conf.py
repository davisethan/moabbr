import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

project = "moabbr"
author = "Ethan Davis"

extensions = [
    "sphinx.ext.autodoc",
    "myst_parser",
]

myst_enable_extensions = ["colon_fence"]

html_static_path = ["_static"]
html_theme = "furo"
html_css_files = ["custom.css"]
