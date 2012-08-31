#!/usr/bin/python
# -*- coding: utf-8 -*-

from ez_setup import use_setuptools
use_setuptools()

from setuptools import setup
setup(
    name='py-sop-extractor',
    version='0.1.0',
    author='codemaniac',
    author_email='ashish.ap.rao@gmail.com',
    packages=['src'],
    url='https://github.com/codemaniac/py-sop-extractor',
    license='LICENSE',
    description='Library and CLI to extract the subject, predicate and object for a given english sentence',
    long_description=open('README').read(),
    keywords = 'NLP subject predicate object',
    install_requires=[
        'simplejson',
        'pyparsing',
        'jpype',
    ]

)
