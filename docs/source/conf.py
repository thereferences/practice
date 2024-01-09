"""
conf.py

Configuration file for the Sphinx documentation builder.

For the full list of built-in configuration values, see the documentation:
https://www.sphinx-doc.org/en/master/usage/configuration.html

Project information
https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
"""

import sphinx_rtd_theme
import sphinx_design
import furo

'''
Basic
'''
project = 'Code of Practice'
copyright = '2023, greyhypotheses'
author = 'greyhypotheses'
release = '0.1'


'''
General configuration
https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
'''
extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.githubpages',
    'sphinx_design'
]


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
'''

html_theme = 'furo'

html_static_path = ['_static']

html_css_files = []

html_js_files = ['https://code.jquery.com/jquery-3.7.0.min.js',
                 'https://code.highcharts.com/stock/highstock.js',
                 'https://code.highcharts.com/stock/modules/data.js',
                 'https://code.highcharts.com/stock/modules/exporting.js',
                 'https://code.highcharts.com/stock/modules/export-data.js',
                 'https://code.highcharts.com/stock/modules/accessibility.js',
                 'https://code.highcharts.com/highcharts.js',
                 'https://code.highcharts.com/modules/networkgraph.js',
                 'js/latex.js']

html_theme_options = {
    'canonical_url': 'https://membranes.github.io/practice/',
    'analytics_id': '',
    'style_external_links': False,
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
}

html_logo = ''

html_context = {
    'landing_page': {
        'menu': [
            {'title': 'Introduction',
             'url': ''},
            {'title': 'Data',
             'url': ''},
            {'title': 'Search',
             'url': 'search.html'}
        ]
    }
}