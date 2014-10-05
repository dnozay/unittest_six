#!/usr/bin/env python

import os
from setuptools import setup, find_packages
from distutils.util import convert_path

# Load version information
main_ns = {}
ver_path = convert_path('src/unittest/version.py')
with open(ver_path, 'rb') as ver_file:
    exec(ver_file.read(), main_ns)


install_requires = ['six>=1.4.0']
tests_require = ['six>=1.8.0']
import sys
if sys.version_info < (2, 7):
    raise RuntimeError('Python version not supported (need 2.7+)')

setup(
    name = 'unittest_six',
    version = main_ns['__version__'],
    description = 'unittest backport',
    install_requires = install_requires,
    tests_require = tests_require,
    license = 'PSF',
    platforms = ['Any'],
    keywords = ['unittest', 'six'],
    url = 'https://github.com/dnozay/unittest_six/',
    classifiers = [
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Python Software Foundation License version 2',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Testing'
    ],
    packages = find_packages('src'),
    package_dir = {'':'src'},
    zip_safe = False,
    include_package_data = True,
    test_suite = 'unittest.test.suite'
)
