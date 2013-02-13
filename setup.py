#!/usr/bin/python
# -*- coding: utf-8 -*-

from ez_setup import use_setuptools
use_setuptools()

from setuptools import setup
setup(
    name='sopex',
    version='0.1.0',
    author='Ashish Prasad (codemaniac)',
    author_email='ashish.ap.rao@gmail.com',
    packages=['sopex'],
    test_suite='tests',
    scripts=['bin/sopex'],
    url='https://github.com/codemaniac/sopex',
    license='LICENSE',
    description='Library and CLI to extract the subject, predicate and object for a given english sentence',
    keywords = 'NLP subject predicate object triplet extraction',
    install_requires=[
        'setuptools',
        'simplejson',
        'pyparsing==1.5',
        'jpype',
        'argparse'
    ],
    dependency_links = [
        'https://github.com/originell/jpype/tarball/master#egg=jpype'
    ]

)
