#!/usr/bin/env python

import re
import os
from distutils.core import setup
from setuptools import find_packages, setup

MODULE_NAME = 'mdx_bootstrap'


def get_version():
    with open(os.path.join(
        os.path.dirname(__file__), MODULE_NAME, '__init__.py')
    ) as init:

        for line in init.readlines():
            res = re.match(r'__version__ *= *[\'"]([0-9a-z\.]*)[\'"]$', line)
            if res:
                return res.group(1)


setup(name='MDX Bootstrap',
      version=get_version(),
      description='Bootstrap for Python-Markdown',
      author='Chris Hua',
      author_email='hua.christopher@gmail.com',
      url='https://github.com/stillmatic/mdx_bootstrap/',
      packages=find_packages(),
      license='MIT',
      install_requires=[
            'markdown',
      ],
      tests_require=[],
      test_suite=MODULE_NAME + '.tests',

)
