"""Created on Sep 7, 2016

This module contains Python object oriented wrapper for synctex_parser C
library. It is based on SWIG generated wrapper to synctex_parser C library.
    
NOTE: Nearly each class and method is documented in a way that docstring
contains information about functions or types from synctex_parser library 
which are used in implementation. If more information is needed please
consult synctex_parser library documentation ('synctex_parser.h' file 
contain verbose commentary which covers library use cases).

Author: Jan Kumor
"""
import enum

import _synctex_parser as _sp

_C_STDOUT_NOTE = """IMPORTANT NOTE: This function targets debugging and 
        development purposes. It uses C level stdout functions which are not
        captured on Python level. In future versions redirecting this display
        to string or stream might be possible (platform specific)."""

_TEX_COORD_DOC = """Expressed in TeX small points coordinates, with origin at
        the top left corner."""
        
_PAGE_COORD_DOC = """Expressed in page coordinates, with origin at
        the top left corner."""

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


class SyncTeXNodeType(enum.Enum):
    """Enum showing types of SyncTeXNodes.
    
    Wraps around synctex_node_type_t enum values from syncex_parser
    library.
    """
    error = _sp.synctex_node_type_error
    input = _sp.synctex_node_type_input
    sheet = _sp.synctex_node_type_sheet
    vbox = _sp.synctex_node_type_vbox
    void_vbox = _sp.synctex_node_type_void_vbox
    hbox = _sp.synctex_node_type_hbox
    void_hbox = _sp.synctex_node_type_void_hbox
    kern = _sp.synctex_node_type_kern
    glue = _sp.synctex_node_type_glue
    math = _sp.synctex_node_type_math
    boundary = _sp.synctex_node_type_boundary


class SyncTeXNode(object):
    """SyncTeXNode is object based wrapper around synctex_node_t pointer.
    """
    
    @classmethod
    def factory(cls, pointer):
        """Creates SyncTeXNode from given C pointer or returns None if
        pointer is NULL.
        """
        return SyncTeXNode(pointer) if pointer else None
         
    def __init__(self, node):
        """Inits SyncTeXNode.
        """
        self._node = node
        
    def __bool__(self):
        """In boolean context SyncTeXNode is True when internal C pointer is
        not None (NULL in C) and False otherwise.
        """
        return self._node is not None
    
    def __str__(self):
        return super().__str__()[:-1] + " is: " + str(self.type) + ">"
    
    @property
    @wrapdoc('synctex_node_parent')
    def parent(self):
        """Getter for node's parent.
        
        {wrapdoc}
        
        Returns:
            SyncTeXNode which is parent of node or None if doesn't have
            parent.
        """
        return SyncTeXNode.factory(_sp.synctex_node_parent(self._node))
    
    @property
    @wrapdoc('synctex_node_sheet')
    def sheet(self):
        """Getter for node's sheet.
        
        {wrapdoc}
        
        Returns:
            SyncTeXNode which is sheet of node or None if doesn't belong to
            sheet.
        """
        return SyncTeXNode.factory(_sp.synctex_node_sheet(self._node))
    
    @property
    @wrapdoc('synctex_node_child')
    def child(self):
        """Getter for node's first child.
        
        First child starts sibling chain containing all children of self.
        However it is possible to iterate all children using neat helper
        property named children.
        
        {wrapdoc}
        
        Returns:
            SyncTeXNode which is first child of node or None if doesn't have
            children.
        """
        return SyncTeXNode.factory(_sp.synctex_node_child(self._node))
    
    @property
    def children(self):
        """Generator of all node's children.
        
        Returns:
            Generator expression yielding consecutive children of node.
        """
        child = self.child
        while child:
            yield child
            child = child.sibling
            
    @property
    @wrapdoc('synctex_node_sibling')
    def sibling(self):
        """Getter for node's sibling.
        
        {wrapdoc}
        
        Returns:
            SyncTeXNode which is sibling of self or None if don't have
            sibling.
        """
        return SyncTeXNode.factory(_sp.synctex_node_sibling(self._node))
    
    @property
    @wrapdoc('synctex_node_type')
    def type(self) -> SyncTeXNodeType:
        """Getter for node's type.
        
        {wrapdoc}
        """
        return SyncTeXNodeType(_sp.synctex_node_type(self._node))
    
    @adddoc(cstdout=_C_STDOUT_NOTE)
    @wrapdoc('synctex_node_log')
    def log(self):
        """Displays node information.
        
        {{cstdout}}
        
        {wrapdoc}
        """
        _sp.synctex_node_log(self._node)
        
    @adddoc(cstdout=_C_STDOUT_NOTE)
    @wrapdoc('synctex_node_display')
    def display(self):
        """Displays node information and recursively for next node.
        
        {{cstdout}}
        
        {wrapdoc}
        
        Wraps around synctex_node_display function from synctex_parser
        library.
        """
        _sp.synctex_node_display(self._node)
    
    @property
    @wrapdoc('synctex_node_charindex')
    def charindex(self) -> int:
        """Returns location of node's definition in synctex file.
        
        {wrapdoc}
        """
        return _sp.synctex_node_charindex(self._node)
        
    @property
    @wrapdoc('synctex_node_tag')
    def tag(self) -> int:
        """Getter for node's tag.
        
        {wrapdoc}
        """
        return _sp.synctex_node_tag(self._node)
    
    @property
    @wrapdoc('synctex_node_line')
    def line(self) -> int:
        """Getter for node's line.
        
        {wrapdoc}
        """
        return _sp.synctex_node_line(self._node)
    
    @property
    @wrapdoc('synctex_node_column')
    def column(self) -> int:
        """Getter for node's column.
        
        {wrapdoc}
        """
        return _sp.synctex_node_column(self._node)
    
    @property
    @wrapdoc('synctex_node_mean_line')
    def mean_line(self) -> int:        
        """For non void horizontal boxes returns average of the line
        numbers of included nodes.
        
        {wrapdoc}
        """
        return _sp.synctex_node_column(self._node)
    
    @property
    @wrapdoc('synctex_node_page')
    def page(self) -> int:
        """Gets output file page number (1 based as TeX standard) on
        which node is.
        
        {wrapdoc}
        """
        return _sp.synctex_node_page(self._node)
    
    @property
    @adddoc(tsp=_TEX_COORD_DOC)
    @wrapdoc('synctex_node_h')
    def h(self) -> int:
        """Horizontal coordinate of node.
        
        {{tsp}}
        
        {wrapdoc}
        """
        return _sp.synctex_node_h(self._node)
    
    @property
    @adddoc(tsp=_TEX_COORD_DOC)
    @wrapdoc('synctex_node_v')
    def v(self) -> int:
        """Vertical coordinate of node.
        
        {{tsp}}
        
        {wrapdoc}
        """
        return _sp.synctex_node_v(self._node)
    
    @property
    @adddoc(tsp=_TEX_COORD_DOC)
    @wrapdoc('synctex_node_width')
    def width(self) -> int:
        """Width of node.
        
        {{tsp}}
        
        {wrapdoc}
        """
        return _sp.synctex_node_width(self._node)
    
    @property
    @adddoc(tsp=_PAGE_COORD_DOC)
    @wrapdoc('synctex_node_visible_h')
    def visible_h(self) -> int:
        """Visible horizontal coordinate of node.
        
        {{tsp}}
        
        {wrapdoc}
        """
        return _sp.synctex_node_visible_h(self._node)
    
    @property
    @adddoc(tsp=_PAGE_COORD_DOC)
    @wrapdoc('synctex_node_visible_v')
    def visible_v(self) -> int:
        """Visible vertical coordinate of node.
        
        {{tsp}}
        
        {wrapdoc}
        """
        return _sp.synctex_node_visible_v(self._node)
    
    @property
    @adddoc(tsp=_PAGE_COORD_DOC)
    @wrapdoc('synctex_node_visible_width')
    def visible_width(self) -> int:
        """Visible width of node.
        
        {{tsp}}
        
        {wrapdoc}
        """
        return _sp.synctex_node_visible_width(self._node)
    
    #
    #GENERATED METHODS
    #
    @property
    @adddoc(tsp=_TEX_COORD_DOC)
    @wrapdoc('synctex_node_box_h')
    def box_h(self):
        """h dimension of node's enclosing box.
        
        {{tsp}}
        
        {wrapdoc}
        """
        return _sp.synctex_node_box_h(self._node)

    @property
    @adddoc(tsp=_TEX_COORD_DOC)
    @wrapdoc('synctex_node_box_v')
    def box_v(self):
        """v dimension of node's enclosing box.
        
        {{tsp}}
        
        {wrapdoc}
        """
        return _sp.synctex_node_box_v(self._node)

    @property
    @adddoc(tsp=_TEX_COORD_DOC)
    @wrapdoc('synctex_node_box_width')
    def box_width(self):
        """width dimension of node's enclosing box.
        
        {{tsp}}
        
        {wrapdoc}
        """
        return _sp.synctex_node_box_width(self._node)

    @property
    @adddoc(tsp=_TEX_COORD_DOC)
    @wrapdoc('synctex_node_box_height')
    def box_height(self):
        """height dimension of node's enclosing box.
        
        {{tsp}}
        
        {wrapdoc}
        """
        return _sp.synctex_node_box_height(self._node)

    @property
    @adddoc(tsp=_TEX_COORD_DOC)
    @wrapdoc('synctex_node_box_depth')
    def box_depth(self):
        """depth dimension of node's enclosing box.
        
        {{tsp}}
        
        {wrapdoc}
        """
        return _sp.synctex_node_box_depth(self._node)

    @property
    @adddoc(tsp=_PAGE_COORD_DOC)
    @wrapdoc('synctex_node_box_visible_h')
    def box_visible_h(self):
        """visible_h dimension of node's enclosing box.
        
        {{tsp}}
        
        {wrapdoc}
        """
        return _sp.synctex_node_box_visible_h(self._node)

    @property
    @adddoc(tsp=_PAGE_COORD_DOC)
    @wrapdoc('synctex_node_box_visible_v')
    def box_visible_v(self):
        """visible_v dimension of node's enclosing box.
        
        {{tsp}}
        
        {wrapdoc}
        """
        return _sp.synctex_node_box_visible_v(self._node)

    @property
    @adddoc(tsp=_PAGE_COORD_DOC)
    @wrapdoc('synctex_node_box_visible_width')
    def box_visible_width(self):
        """visible_width dimension of node's enclosing box.
        
        {{tsp}}
        
        {wrapdoc}
        """
        return _sp.synctex_node_box_visible_width(self._node)

    @property
    @adddoc(tsp=_PAGE_COORD_DOC)
    @wrapdoc('synctex_node_box_visible_height')
    def box_visible_height(self):
        """visible_height dimension of node's enclosing box.
        
        {{tsp}}
        
        {wrapdoc}
        """
        return _sp.synctex_node_box_visible_height(self._node)

    @property
    @adddoc(tsp=_PAGE_COORD_DOC)
    @wrapdoc('synctex_node_box_visible_depth')
    def box_visible_depth(self):
        """visible_depth dimension of node's enclosing box.
        
        {{tsp}}
        
        {wrapdoc}
        """
        return _sp.synctex_node_box_visible_depth(self._node)
        
    
class SyncTeXScanner(object):
    """SyncTeXScanner is object based wrapper class around synctex_scanner_t
    pointer. 
    
    SyncTeXScanner provides convenient way of using scanner related 
    functions from C synctex_parser library.
    
    To avoid manual freeing internal C object SyncTeXScanner is implemented
    as context manager which makes it compatible with 'with' Python
    statement. Leaving context frees internal C object automatically.
    """

    def __init__(self, output_file, build_directory=None, pars=1):
        """Inits SyncTeXScanner.
        """
        self.output_file = output_file
        self._scanner = _sp.synctex_scanner_new_with_output_file(output_file,
                                                                 build_directory,
                                                                 pars)
    
    def __str__(self):
        return super().__str__()[:-1] + "; file: '" + self.output_file + "'>"
    
    #Context manager magic methods __enter__ and __exit__
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, traceback):
        """We must free inner C object.
        """
        self._cleanup()
    
    def _cleanup(self):
        """Frees internal C object.
        """
        _sp.synctex_scanner_free(self._scanner)
        self._scanner = None  
    
    #Wrappers            
    def parse(self) -> None:
        """Used to manually assure that scanner did the parsing process.
        
        For more information check documentation of synctex_scanner_parse
        function from synctex_parser library. 
        
        Raises:
            RuntimeError when parsing fails.
        """
        self._scanner = _sp.synctex_scanner_parse(self._scanner)
        if not self._scanner:
            raise RuntimeError('{}: There was a problem while parsing file.'
                               .format(self))
            
    def display_query(self, file_name, line, column) -> list:
        """Given the file name, a line and a column number returns list of
        nodes satisfying constrain.
        
        Internally uses synctex_display_query function for making query and  
        synctex_next_result function when constructing result list ( both
        functions belong to synctex_parser library). For more information 
        check their documentation.
        
        Arguments:
            file_name: Name of TeX input file which will be queried.
            line: Input file line number which will be queried.
            column: Line column which will be queried.
            
        Returns:
            List of SyncTeXNode objects satisfying query constrain.
            
        Raises:
            RuntimeError when query fails.
        """
        #TODO: custom exception
        status = _sp.synctex_display_query(self._scanner, file_name,
                                                   line, column)
        if status < 0:
            raise RuntimeError("{}: Failed to query {}:{}:{}. Status={}"
                               .format(self, file_name, line, column, status))
        
        nodes = []
        #apparently this is python idiomatic way of iterating
        while True: 
            node_ptr = _sp.synctex_next_result(self._scanner)
            if node_ptr:
                nodes.append(SyncTeXNode(node_ptr))
            else:
                break
        return nodes
    
    def edit_query(self, page, h, v) -> list:
        """Given page number, vertical and horizontal coordinates returns list of
        nodes satisfying constrain. Page number is 1 based (counting starts
        from 1). Coordinates are in 72 dpi units and relative to top left
        corner of the page.
        
        Internally uses synctex_edit_query function for making query and  
        synctex_next_result function when constructing result list ( both
        functions belong to synctex_parser library). For more information 
        check their documentation.
        
        Arguments:
            page: Number of output file page which will be queried ( 1 based)
            h: Horizontal coordinate which will be queried.
            v: Vertical coordinate which will be queried.
            
        Returns:
            List of SyncTeXNode objects satisfying query constrain.
            
        Raises:
            RuntimeError when query fails.
        """
        #TODO: custom exception
        if page < 1:
            raise ValueError("Page number must be greater then 0.")
        status = _sp.synctex_edit_query(self._scanner, page, h, v)
        if status < 0:
            raise RuntimeError("{}: Failed to query {}:{}:{}. Status={}"
                               .format(self, page, h, v, status))
        
        nodes = []
        #apparently this is python idiomatic way of iterating
        while True: 
            node_ptr = _sp.synctex_next_result(self._scanner)
            if node_ptr:
                nodes.append(SyncTeXNode(node_ptr))
            else:
                break
        return nodes
    
    @adddoc(cstdout=_C_STDOUT_NOTE)
    def display(self) -> None:
        """Displays all information contained in scanner object. 
        
        {cstdout}
        
        Wrapper for synctex_scanne_display function from synctex_parser
        library.
        """
        _sp.synctex_scanner_display(self._scanner)
                    
    @property
    def x_offset(self) -> int:
        """Gets x offset of the origin in TeX coordinates. 
        
        Wraps around synctex_scanner_x_offset function from synctex_parser
        library.
        
        Returns:
            Origin's x offset value.
        """
        return _sp.synctex_scanner_x_offset(self._scanner)
    
    @property
    def y_offset(self) -> int:
        """Gets y offset of the origin in TeX coordinates. 
        
        Wraps around synctex_scanner_y_offset function from synctex_parser
        library.
        
        Returns:
            Origin's y offset value.
        """
        return _sp.synctex_scanner_y_offset(self._scanner)

    @property
    def magnification(self) -> float:
        """Gets magnification of the origin. 
        
        Wraps around synctex_scanner_magnification function from 
        synctex_parser library.
        
        Returns:
            Origin's magnification value.
        """
        return _sp.synctex_scanner_y_offset(self._scanner)
    
    def get_name(self, tag: int) -> str:
        """Retrieves file name corresponding to tag.
        
        Wraps around syctex_scanner_get_name function from synctex_parser
        library.
        
        Returns:
            File name corresponding to tag.
        """
        return _sp.synctex_scanner_get_name(self._scanner, tag)
    
    def get_tag(self, name: str) -> int:
        """Retrieves tag corresponding to file name.
        
        Wraps around syctex_scanner_get_tag function from synctex_parser
        library.
        
        Returns:
            Tag corresponding to file name.
        """
        return _sp.synctex_scanner_get_tag(self._scanner, name)    

    @property
    def input(self):
        """Getter for first input node of scanner.
        
        Wraps around syctex_scanner_input function from synctex_parser
        library.
        
        Returns:
            SyncTeXNode being first input node of scanner.
        """
        return SyncTeXNode(_sp.synctex_scanner_input(self._scanner))
        
    @property
    def inputs(self):
        """Generator of all scanner's input nodes. Provides convenient way
        of iterating input nodes.
        
        Returns:
            Generator expression which yields input nodes of scanner.
        """
        input_node = self.input
        while input_node:
            yield input_node
            input_node = input_node.sibling 
    
    @property    
    def output(self) -> str:
        """Getter for name which was used to create scanner.
        
        Wraps aroound synctex_scanner_get_output function from
        synctex_parser library.
        
        Returns:
            Name of file used to create scanner.
        """
        return _sp.synctex_scanner_get_output(self._scanner)
    
    @property
    def synctex(self) -> str:
        """Getter for synctex file.
        
        Wraps aroound synctex_scanner_get_synctex function from
        synctex_parser library.
        
        Returns:
            Name of synctex file.
        """
        return _sp.synctex_scanner_get_synctex(self._scanner)

        
if __name__ == '__main__':
#SERVES AS TEST SUITE
    with SyncTeXScanner('example/_build/presentation.pdf') as scanner:
        #Scanner
        print("SCANNER")
        print(scanner)
        query = scanner.display_query('presentation.tex', 50, 1)
        print(query)
        node = query[0]
        print(scanner.edit_query(5, 0.5, 0.5))
        print(scanner.x_offset)
        print(scanner.y_offset)
        print(scanner.magnification)
        print(scanner.get_name(142))
        print(scanner.get_tag('/tmp/tmp588prwyq_rapidbeamer/./presentation.tex'))
        print(scanner.input)
        print(len(list(scanner.inputs)))
        print(scanner.output)
        print(scanner.synctex)
        #help(SyncTeXScanner)
        #Node type
        print("NODE TYPE")
        print(SyncTeXNodeType.error.value)
        #help(SyncTeXNodeType)
        #Node
        print("NODE: %s" % node)
        print("PARENT: %s" % node.parent)
        print("SHEET %s" % node.sheet)
        print("CHILD: %s" % node.child)
        print("CHILDREN: %s" % list(node.children))
        print("TYPE: %s" % node.type)
        print()
        node.log()
        print()
        node.display()
        print()
        print("CHARINDEX %d" % node.charindex)
        print("TAG: %d" % node.tag)
        print("LINE: %d" % node.line)
        print("COLUMN: %d" % node.column)
        print("PAGE: %d" % node.page)
        print("H: %d" % node.h)
        print("V: %d" % node.v)
        print("WIDTH: %d" % node.width)
        print("VIS H: %d" % node.visible_h)
        print("VIS V: %d" % node.visible_v)
        print("VIS WIDTH: %d" % node.visible_width)
        #help(SyncTeXNode)