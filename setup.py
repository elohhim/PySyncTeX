if __name__ == '__main__':
    from setuptools import setup, Extension
    
    _synctex_parser = Extension('pysynctex._synctex_parser',
                                sources=['wrapper/synctex_parser.i',
                                'wrapper/synctex_package/synctex_parser.c',
                                'wrapper/synctex_package/synctex_parser_utils.c'],
                                include_dirs=['wrapper/synctex_package'])
    
    setup(name='PySyncTeX',
          version='0.2.0',
          author='Jan Kumor',
          author_email='jan.kumor@gmail.com',
          description='Python wrapper for SyncTeX parser C library.',
          long_description=open('README.rst').read(),
          url='https://github.com/elohhim/PySyncTeX',
          license="MIT",
          platforms='ANY',
          packages=['pysynctex'],
          ext_modules=[_synctex_parser],
          classifiers=[
            'Development Status :: 3 - Alpha',
            'Intended Audience :: Developers',
            'Programming Language :: Python :: 3',
            'License :: OSI Approved :: MIT License',
            'Operating System :: POSIX :: Linux',
            'Natural Language :: English',
            'Topic :: Software Development :: Libraries :: Python Modules',
            'Topic :: Text Processing :: Markup :: LaTeX',
            ]
          )
