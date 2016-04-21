#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='mcastsocket',
    version='1.0.0',
    description="Provides a simple interface for configuring multicast socket services",
    long_description=readme + '\n\n' + history,
    author="Mike C. Fletcher",
    author_email='mcfletch@vrplumber.com',
    url='https://github.com/mcfletch/mcastsocket',
    packages=[
        'mcastsocket',
    ],
    package_dir={'mcastsocket':
                 'mcastsocket'},
    include_package_data=True,
    install_requires=requirements,
    license="LGPL",
    zip_safe=False,
    keywords='mcastsocket',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Lesser General Public License v2 (LGPLv2)',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
