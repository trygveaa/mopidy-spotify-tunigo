from __future__ import unicode_literals

import re

from setuptools import find_packages, setup


def get_version(filename):
    content = open(filename).read()
    metadata = dict(re.findall("__([a-z]+)__ = '([^']+)'", content))
    return metadata['version']


setup(
    name='Mopidy-Spotify-Tunigo',
    version=get_version('mopidy_spotify_tunigo/__init__.py'),
    url='https://github.com/trygveaa/mopidy-spotify-tunigo',
    license='Apache License, Version 2.0',
    author='Trygve Aaberge',
    author_email='trygveaa@gmail.com',
    description='Mopidy extension for providing the browse feature of Spotify',
    long_description=open('README.rst').read(),
    packages=find_packages(exclude=['tests', 'tests.*']),
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        'setuptools',
        'Mopidy >= 0.19.0',
        'Pykka >= 1.1',
        'mopidy-spotify >= 1.2.0',
        'tunigo',
    ],
    test_suite='nose.collector',
    tests_require=[
        'nose',
        'mock >= 1.0',
    ],
    entry_points={
        'mopidy.ext': [
            'spotify_tunigo = mopidy_spotify_tunigo:Extension',
        ],
    },
    classifiers=[
        'Environment :: No Input/Output (Daemon)',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Topic :: Multimedia :: Sound/Audio :: Players',
    ],
)
