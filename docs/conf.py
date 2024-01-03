# Configuration file for the Sphinx documentation builder.

# -- Project information

project = "AndroidIDE"
copyright = "2023, The AndroidIDE Project"
author = "AndroidIDE"
github_user = "AndroidIDEOfficial"
github_repo = "docs"
github_version = "main"

release = "2.7"
version = "2.7.0-beta"

# -- General configuration

extensions = [
    "sphinx.ext.duration",
    "sphinx.ext.doctest",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    "sphinx_rtd_dark_mode",
]

intersphinx_mapping = {}

intersphinx_disabled_domains = ["std"]

source_suffix = {".rst": "restructuredtext", ".md": "markdown"}

templates_path = ["_templates"]

# -- Options for HTML output

html_theme = "sphinx_rtd_theme"
html_theme_options = {
    "vcs_pageview_mode": "blob",
}
html_context = {
    "display_github": True,
    "github_user": github_user,
    "github_repo": github_repo,
    "github_version": github_version,
    "conf_py_path": "/docs/",
}

html_static_path = ["_static"]
