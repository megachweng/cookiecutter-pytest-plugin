#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs
from setuptools import setup


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding='utf-8').read()


setup(
    name='pytest-{{cookiecutter.plugin_name}}',
    version='{{cookiecutter.version}}',
    author='{{cookiecutter.full_name}}',
    author_email='{{cookiecutter.email}}',
    maintainer='{{cookiecutter.full_name}}',
    maintainer_email='{{cookiecutter.email}}',
    license='{{cookiecutter.license}}',
    url='https://github.com/{{cookiecutter.github_username}}/pytest-{{cookiecutter.plugin_name}}',
    description='{{cookiecutter.short_description}}',
    long_description=read('README.md'),
    long_description_content_type="text/markdown",
    py_modules=['pytest_{{cookiecutter.module_name}}'],
    python_requires='>=3.6.5',
    install_requires=['pytest>={{cookiecutter.pytest_version}}'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Pytest',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Operating System :: OS Independent',
        {% if cookiecutter.license == "MIT" -%}
        'License :: OSI Approved :: MIT License',
        {%- elif cookiecutter.license == "BSD-3" -%}
        'License :: OSI Approved :: BSD License',
        {%- elif cookiecutter.license == "GNU GPL v3.0" -%}
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        {%- elif cookiecutter.license == "Apache Software License 2.0" -%}
        'License :: OSI Approved :: Apache Software License',
        {%- elif cookiecutter.license == "Mozilla Public License 2.0" -%}
        'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
        {%- endif %}
    ],
    entry_points={
        'pytest11': [
            '{{cookiecutter.plugin_name}} = pytest_{{cookiecutter.module_name}}',
        ],
    },
)
