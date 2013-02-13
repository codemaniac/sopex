#!/usr/bin/python
# -*- coding: utf-8 -*-

from ez_setup import use_setuptools
use_setuptools()

from setuptools import setup
setup(
    name='sopex',
    version='0.1',
    author='Ashish Prasad (codemaniac)',
    author_email='ashish.ap.rao@gmail.com',
    packages=['sopex'],
    test_suite='tests',
    scripts=['bin/sopex'],
    url='https://github.com/codemaniac/sopex',
    license='LICENSE',
    description='Library and CLI to extract the subject, predicate and object for a given english sentence',
    keywords = 'NLP subject predicate object triplet extraction',
    install_requires=['simplejson', 'jpype==0.5.4.2', 'argparse', 'pyparsing==1.5'],
    dependency_links = [
        'https://github.com/originell/jpype/tarball/master#egg=jpype-0.5.4.2'
    ]

)
