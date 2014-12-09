#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup

setup(
    name = 'qwak',
    version = '0.3',
    url = 'https://github.com/c0ding/qwak',
    download_url = 'https://github.com/c0dingqwak/archive/master.zip',
    author = 'c0ding',
    author_email = 'me@martinsimon.me',
    license = 'Apache v2.0 License',
    packages = ['qwak'],
    description = 'Python API wrapper for MPOS.',
    long_description = file('README.md','r').read(),
    keywords = ['MPOS', 'Mining Portal Open Source', 'Scrypt', 'SHA256d', 'cryptocurrency', 'API'],
)
