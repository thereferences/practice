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

'''
Basic
'''
project = 'Code of Practice'
project_copyright = '2024, The Artificial Intelligence Unit'
author = '@greyhypotheses'
release = 'v0.1.8'


'''
General configuration
https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
https://myst-parser.readthedocs.io/en/v0.15.1/sphinx/intro.html#install-a-new-sphinx-extension-and-use-its-functionality
'''
extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.githubpages',
    'sphinx.ext.mathjax',
    'sphinx_design',
    'sphinxcontrib.mermaid',
    "sphinx.ext.intersphinx",
    "sphinx.ext.viewcode",
    'myst_parser'
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


'''
https://myst-parser.readthedocs.io/en/latest/configuration.html
'''
myst_heading_anchors = 4


'''
Mathematics
'''
mathjax_path = 'https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js'
myst_dmath_double_inline = True


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

html_static_path = ['_static']

html_css_files = ['css/figures.css',
                  'https://unpkg.com/tabulator-tables/dist/css/tabulator.min.css',
                  'https://cdnjs.cloudflare.com/ajax/libs/flickity/3.0.0/flickity.min.css',
                  'css/slides.css',
                  'css/generic.css',
                  'https://cdnjs.cloudflare.com/ajax/libs/prism/9000.0.1/themes/prism.min.css']

html_js_files = ['https://code.jquery.com/jquery-3.7.0.min.js',
                 'https://code.highcharts.com/stock/highstock.js',
                 'https://code.highcharts.com/stock/modules/data.js',
                 'https://code.highcharts.com/stock/modules/exporting.js',
                 'https://code.highcharts.com/stock/modules/export-data.js',
                 'https://code.highcharts.com/stock/modules/accessibility.js',
                 'https://code.highcharts.com/highcharts.js',
                 'https://code.highcharts.com/modules/networkgraph.js',
                 'https://viewer.diagrams.net/js/viewer-static.min.js',
                 'https://cdnjs.cloudflare.com/ajax/libs/flickity/3.0.0/flickity.pkgd.min.js',
                 'https://cdnjs.cloudflare.com/ajax/libs/prism/9000.0.1/prism.min.js'
                 ]

html_theme_options = {
    'use_download_button': True,
    'use_fullscreen_button': True,
    'home_page_in_toc': True,
    'show_navbar_depth': 1,
    'max_navbar_depth': 4,
    'collapse_navbar': False,
    'toc_title': 'PRACTICE',
    'show_toc_level': 2,
    'sidebarwidth': 250
}

html_context = {
    'landing_page': {
        'menu': [
            {'title': 'Introduction',
             'url': ''},
            {'title': 'Technologies & Development Practices',
             'url': ''}
        ]
    }
}
