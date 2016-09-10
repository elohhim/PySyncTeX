from distutils.core import setup, Extension

_synctex_parser = Extension('_synctex_parser',
                            sources=['synctex_parser.i',
                            'lib/synctex_parser.c',
                            'lib/synctex_parser_utils.c'],
                            include_dirs=['lib'])

setup(name='PySyncTeX',
      version='0.1.1',
      author='Jan Kumor',
      author_email='jan.kumor@gmail.com',
      url='github.com/elohhim/pysynctex',
      license="MIT",
      description='SyncTeX parser library wrapper for Python.',
      platform='ANY',
      ext_modules=[_synctex_parser])
