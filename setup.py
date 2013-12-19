#!/usr/bin/env python

"""
Setup script for Pasty.
"""

import setuptools

from pasty import __project__

# Touch the README, it will be generated on release
README = 'README.rst'
import os
if not os.path.exists(README):
    open(README, 'wb').close()


setuptools.setup(
    name=__project__,
    version='0.0.0',

    description="Serverless state management using online text services.",
    url='https://github.com/jacebrowning/pasty',
    author='Jace Browning',
    author_email='jacebrowning@gmail.com',

    packages=setuptools.find_packages(),

    entry_points={'console_scripts': []},

    long_description=open(README).read(),
    license='LGPL',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',  # pylint: disable=C0301
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Topic :: Games/Entertainment',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],

    install_requires=[],
)
