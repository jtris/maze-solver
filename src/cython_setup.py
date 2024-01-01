from setuptools import Extension, setup
from Cython.Build import cythonize
import numpy


ext_modules = [
    Extension(
        'grid_dijkstras_algorithm',
        ['grid_dijkstras_algorithm.pyx'],
        compiler_directives={'language_level':'3'},
        include_dirs=[numpy.get_include()]
    )
]

setup(    
    ext_modules=cythonize(ext_modules)    
)
