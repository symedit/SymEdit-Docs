# -*- coding: utf-8 -*-
import sys
import os

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
html_theme = 'symedit_rtd_theme'
html_theme_path = ['_themes']
htmlhelp_basename = 'SymEditdoc'
man_pages = [
    ('index', 'symedit', u'SymEdit Documentation',
     [u'Craig Blanchette'], 1)
]
