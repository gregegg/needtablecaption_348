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
from pathlib import Path

# -- Project information -----------------------------------------------------

project = 'needextract'
copyright = ''
author = 'G. Troyer'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinxcontrib.needs', 'sphinxcontrib.plantuml']


numfig = True  # figures, tables and code-blocks are automatically numbered if they have a caption.

# ---------- Sphinx Needs configuration --------------------------

plantuml_path = Path(sys.executable).parent.joinpath('plantuml.jar')  #assumes that plantuml.jar is located in same directory as python executable
plantuml = 'java -jar %s' % plantuml_path
graphviz_path = str(Path(sys.executable).parent.joinpath('dot'))
os.putenv('GRAPHVIZ_DOT', graphviz_path)
plantuml_output_format = 'png'
needs_table_style = "datatables"

# Define a directive for User Inputs (to be compiled in the User's Manual).
# Taken from https://sphinxcontrib-needs.readthedocs.io/en/latest/configuration.html#needs-types

needs_id_regex = '^[A-Z0-9_.]{3,}'
needs_types = [dict(directive="req", title="Requirement", prefix="R_", color="#BFD8D2", style="node"),
               dict(directive="spec", title="Specification", prefix="S_", color="#FEDCD2", style="node"),
               dict(directive="user", title="User Requirement", prefix="U_", color="#DF744A", style="node"),
               dict(directive="test", title="Test Case", prefix="T_", color="#DCB239", style="node"),
               # Kept for backwards compatibility
               dict(directive="need", title="Need", prefix="N_", color="#9856a5", style="node")
               ]

needs_role_need_template = "{id}"

# # # ----- Options for LaTeX output ----------------------------------------------

latex_elements = {
    # The paper size ('letter' or 'a4').
    # 'latex_paper_size': 'letter',
    'classoptions' : ',openany,oneside',  #eliminates a bunch of empty pages
#
#     # The font size ('10pt', '11pt' or '12pt').
    'pointsize': '11pt',
# #
# #     # Additional stuff for the LaTeX preamble.
    # note that the '%' starts a raw latex comment
    'preamble':
r'''\DeclareUnicodeCharacter{2588}{ }  % this character was causing grief
    ''',
    'figure_align' : 'H'  # keeps the figures directly in line with the headings.
 }
# #
# # Grouping the document tree into LaTeX files. List of tuples
# # (source start file, target name, title, author, document class
# # [howto/manual]).
latex_documents = [
   ('srd_main', 'SRD.tex', 'Software Requirements Document',
    'G. Troyer', 'manual')
    ]