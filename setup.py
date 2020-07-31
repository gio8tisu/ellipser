#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='ellipsis',
      version='0.1',
      description='Limits the width of lines',
      author='Sergio Garcia Campderrich',
      author_email='gio8.tisu@gmail.com',
      url='https://github.com/gio8tisu/ellipser',
      license='GNU General Public License v3 or later (GPLv3+)',
      py_modules=['ellipsis'],
      scripts=['ellipser'],
      test_suite='test_ellipsis',
)

