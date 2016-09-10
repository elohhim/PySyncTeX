from distutils.core import setup, Extension

_synctex_parser = Extension('_synctex_parser',
                            sources=['wrapper/synctex_parser.i',
                            'wrapper/synctex_package/synctex_parser.c',
                            'wrapper/synctex_package/synctex_parser_utils.c'],
                            include_dirs=['wrapper/synctex_package'])

setup(name='PySyncTeX',
      version='0.2.0',
      author='Jan Kumor',
      author_email='jan.kumor@gmail.com',
      url='github.com/elohhim/pysynctex',
      license="MIT",
      description='Python wrapper for SyncTeX parser C library.',
      platform='ANY',
      ext_modules=[_synctex_parser])
