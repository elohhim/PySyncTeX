/* synctex_parser.i */
%module synctex_parser
%{
/* Headers and declarations */
#include "synctex_parser.h"
%}

/*
synctex_scanner_t synctex_scanner_new_with_output_file(const char * output, const char * build_directory, int parse);
void synctex_scanner_free(synctex_scanner_t scanner);
synctex_scanner_t synctex_scanner_parse(synctex_scanner_t scanner);
synctex_status_t synctex_display_query(synctex_scanner_t scanner,const char *  name,int line,int column);
synctex_status_t synctex_edit_query(synctex_scanner_t scanner,int page,float h,float v);
synctex_node_t synctex_next_result(synctex_scanner_t scanner);
void synctex_scanner_display(synctex_scanner_t scanner);
*/

%include "lib/synctex_parser.h"