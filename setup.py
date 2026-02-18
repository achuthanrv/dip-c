#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Setup configuration for dip-c package.

This setup.py is compatible with both Python 2.7+ and Python 3.x
for potential bioconda packaging.
"""

from __future__ import print_function
import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# Read version from VERSION file
version_file = os.path.join(os.path.dirname(__file__), 'VERSION')
with open(version_file, 'r') as f:
    version = f.read().strip()

# Read long description from README
readme_file = os.path.join(os.path.dirname(__file__), 'README.md')
try:
    with open(readme_file, 'r') as f:
        long_description = f.read()
    long_description_content_type = 'text/markdown'
except IOError:
    long_description = 'Diploid Chromatin Conformation Capture'
    long_description_content_type = 'text/plain'

# Determine Python version-specific requirements
if sys.version_info[0] == 2:
    python_requires = '>=2.7, <3'
    install_requires = [
        'numpy<1.17',  # Last version supporting Python 2.7
        'scipy<1.3',   # Last version supporting Python 2.7
    ]
else:
    python_requires = '>=3.6'
    install_requires = [
        'numpy<2',
        'scipy<1.12',
    ]

setup(
    name='dip-c',
    version=version,
    description='Diploid Chromatin Conformation Capture - 3D genome structure reconstruction from single cells',
    long_description=long_description,
    long_description_content_type=long_description_content_type,
    author='Longzhi Tan',
    author_email='lztan@ucla.edu',
    maintainer='Darrin Schultz',
    maintainer_email='darrin.schultz@gmail.com',
    url='https://github.com/tanlongzhi/dip-c',
    project_urls={
        'Original Repository': 'https://github.com/tanlongzhi/dip-c',
        'Maintained Fork': 'https://github.com/conchoecia/dip-c',
        'Documentation': 'https://github.com/tanlongzhi/dip-c/blob/master/README.md',
    },
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
    python_requires=python_requires,
    py_modules=['dip_c_version'],
    scripts=['dip-c'],
    install_requires=install_requires,
    extras_require={
        'dev': [
            'pytest',
            'pytest-cov',
            'coverage',
        ],
        '3d': [
            'rmsd',  # For 3D structure reconstruction
        ],
    },
    include_package_data=True,
    zip_safe=False,
)
