# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.append(os.path.abspath('../danspeech'))
sys.path.append(os.path.abspath('../../example_scripts'))


# -- Project information -----------------------------------------------------

project = 'DanSpeech'
copyright = '2019, Martin Carsten Nielsen, Rasmus Arpe Fogh Jensen'
author = 'Martin Carsten Nielsen, Rasmus Arpe Fogh Jensen'

# The full version, including alpha/beta/rc tags
release = '1.0.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['recommonmark',
              'sphinx_rtd_theme',
              'sphinx.ext.autodoc',
              'sphinx.ext.autosummary',
              'sphinx_gallery.gen_gallery']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

html_theme_options = {
    'sticky_navigation': False
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

autodoc_member_order = 'bysource'

sphinx_gallery_conf = {
     'examples_dirs': '../example_scripts',     # path to your example scripts
     'gallery_dirs': 'auto_examples',
    'filename_pattern': '/execute_',
    'expected_failing_examples': ['../example_scripts/plot_recognize.py']# path where to save gallery generated examples
}