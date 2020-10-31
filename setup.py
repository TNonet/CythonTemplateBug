from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize


examples_extension = Extension(
    name="test",
    sources=["cy_test.pyx", "test.cpp"],
    include_dirs=[],
    language="c++",
    extra_compile_args=["-std=c++11"],
    extra_link_args=["-std=c++11"]
)
setup(
    name="test",
    ext_modules=cythonize([examples_extension], language_level=3)
)