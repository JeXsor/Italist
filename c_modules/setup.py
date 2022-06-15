from setuptools import setup
from Cython.Build import cythonize

setup(
    name='functions',
    ext_modules=cythonize("functions.pyx"),
    zip_safe=False,
    compiler_directives={'language_level' : "3"}
)