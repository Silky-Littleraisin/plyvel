from setuptools import setup
from setuptools.extension import Extension

setup(name="leveldb-cython",
      version="0.1",
      author="Wouter Bolsterlee",
      author_email="uws@xs4all.nl",
      ext_modules = [Extension("leveldb", ["leveldb.cpp"])]
)