"""
This is conf.py

Notes
-----

Configuration file for the Sphinx documentation builder.

For the full list of built-in configuration values, see the documentation:
https://www.sphinx-doc.org/en/master/usage/configuration.html.

Project information
https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

"""

# Libraries
import os
import sys
import datetime


'''
Path

sys.path.insert(0, os.path.abspath('../..'))
sys.path.append(os.path.join(os.path.dirname(__file__), '../../revitron'))
'''


'''
Master
'''
master_doc = 'index'


'''
Basic
'''
project = '&nbsp; <span style="vertical-align: super; padding-top: 0; padding-bottom: 20px">Code of Practice</span>'
project_copyright = '{}, The Artificial Intelligence Unit'.format(datetime.datetime.now().year)
author = '@greyhypotheses'


'''
General configuration
https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
https://myst-parser.readthedocs.io/en/v0.15.1/sphinx/intro.html#install-a-new-sphinx-extension-and-use-its-functionality
'''
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'autodocsumm',
    'sphinxcontrib.httpdomain',
    'sphinxext.opengraph',
    'sphinxcontrib.jquery',
    'myst_parser',
    'sphinx.ext.duration',
    'sphinx_design',
    'sphinxcontrib.mermaid'
]

myst_enable_extensions = [
    'amsmath',
    'attrs_inline',
    'colon_fence',
    'deflist',
    'dollarmath',
    'fieldlist',
    'html_admonition',
    'html_image',
    'replacements',
    'smartquotes',
    'strikethrough',
    'substitution',
    'tasklist',
    'attrs_block'
]

myst_heading_anchors = 4

add_module_names = False


'''
Mathematics
'''
mathjax_path = 'https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js'
myst_dmath_double_inline = True


'''
Code
'''
pygments_style = 'sphinx'


'''
Paths that contain templates, relative to this directory.
'''
templates_path = ['_templates']


'''
List of patterns, relative to source directory, that match files and
directories to ignore when looking for source files.
This pattern also affects html_static_path and html_extra_path.
'''
exclude_patterns = []


'''
Options for HTML output
https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
'style_nav_header_background': '#343131'
'''

html_theme = 'sphinx_book_theme'

html_theme_options = {
    'show_prev_next': True,
    'secondary_sidebar_items': ['page-toc', 'edit-this-page'],
    'collapse_navigation': True,
    'navigation_depth': 3
}

html_static_path: list[str] = ['_static']

html_css_files: list[str] = [
    'https://unpkg.com/tabulator-tables/dist/css/tabulator.min.css',
    'css/custom.css',
    'css/tooltips.css',
    'css/slides.css',
    'css/generic.css',
    'https://unpkg.com/flickity@2/dist/flickity.min.css',
    'https://cdnjs.cloudflare.com/ajax/libs/prism/9000.0.1/themes/prism.min.css']

html_js_files: list[str] = [
    'https://code.jquery.com/jquery-3.7.0.min.js',
    'https://code.highcharts.com/stock/highstock.js',
    'https://code.highcharts.com/stock/modules/data.js',
    'https://code.highcharts.com/stock/modules/exporting.js',
    'https://code.highcharts.com/stock/modules/export-data.js',
    'https://code.highcharts.com/stock/modules/accessibility.js',
    'https://code.highcharts.com/highcharts.js',
    'https://code.highcharts.com/modules/networkgraph.js',
    'https://viewer.diagrams.net/js/viewer-static.min.js',
    'https://unpkg.com/flickity@2/dist/flickity.pkgd.min.js',
    'https://cdnjs.cloudflare.com/ajax/libs/prism/9000.0.1/prism.min.js',
    'js/slides.js']

html_title = 'CODE OF PRACTICE'

html_favicon = '_static/favicon.ico'

html_context = {
    'landing_page': {
        'menu': [
            {'title': '<b>Parent</b>',
             'url': 'https://github.com/theartificialintelligenceunit'},
            {'title': '<b>About</b>',
             'url': 'about.html'}
        ]
    },
    'display_github': True,
    'github_repo': 'thereferences/practice',
    'conf_py_path': 'develop/docs/source/'
}

html_sidebars = {}


'''
Options for intersphinx extension
https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html#configuration
'''
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
}
