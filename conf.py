# -*- coding: utf-8 -*-
import sys
import os
import sphinx_rtd_theme

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.pngmath',
    'sphinx.ext.ifconfig',
]

source_suffix = '.rst'
master_doc = 'index'
project = u'SymEdit'
copyright = u'2014, Craig Blanchette'
version = ''
release = ''
exclude_patterns = []
html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
htmlhelp_basename = 'SymEditdoc'
man_pages = [
    ('index', 'symedit', u'SymEdit Documentation',
     [u'Craig Blanchette'], 1)
]
