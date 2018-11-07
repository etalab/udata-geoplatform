#!/usr/bin/env python
import os
import io
import re

from setuptools import setup, find_packages

RE_BADGE = re.compile(r'^\[\!\[(?P<text>.*?)\]\[(?P<badge>.*?)\]\]\[(?P<target>.*?)\]$', re.M)

BADGES_TO_KEEP = []


def md(filename):
    '''
    Load .md (markdown) file and sanitize it for PyPI.
    '''
    content = io.open(filename).read()

    for match in RE_BADGE.finditer(content):
        if match.group('badge') not in BADGES_TO_KEEP:
            content = content.replace(match.group(0), '')

    return content


long_description = '\n'.join((
    md('README.md'),
    md('CHANGELOG.md'),
    ''
))


def pip(filename):
    """Parse pip reqs file and transform it to setuptools requirements."""
    return open(os.path.join('requirements', filename)).readlines()


long_description = '\n'.join((
    md('README.md'),
    md('CHANGELOG.md'),
    ''
))

install_requires = pip('install.pip')
tests_require = pip('test.pip')


setup(
    name='udata-geoplatform',
    version=__import__('udata_geoplatform').__version__,
    description=__import__('udata_geoplatform').__description__,
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/opendatateam/udata-geoplatform',
    author='Open Data Team',
    author_email='contact@opendata.team',
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    python_requires='>=3.5',
    tests_require=tests_require,
    extras_require={
        'test': tests_require,
    },
    entry_points={
        'udata.preview': [
            'geoplatform = udata_geoplatform.preview:GeoplatformPreview',
        ],
    },
    license='AGPL',
    zip_safe=False,
    keywords='udata, harvester, uData Geoplatform connector',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python',
        'Environment :: Web Environment',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Topic :: System :: Software Distribution',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
