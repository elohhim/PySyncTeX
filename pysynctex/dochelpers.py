"""Created on Sep 10, 2016

Module containing some helper functions for docstring creation in PySyncTeX.

Author: Jan Kumor
"""

def wrapdoc(function_name):
    def real_wrapsdoc(function):
        wrapdoc = ("""Synctex parser library function wrapped:
            - {}
        Consult 'synctex_parser.h' documentation for more information."""
                   .format(function_name))
        return adddoc(wrapdoc=wrapdoc)(function)
    return real_wrapsdoc

def adddoc(**docstrings):
    """Adds docstrings to function __doc__.
    """
    def real_adddoc(function):
        new_doc = function.__doc__.format(**docstrings)
        function.__doc__ = new_doc
        return function
    return real_adddoc


        