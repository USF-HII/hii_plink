#!/usr/bin/env python

import setuptools

import hii_plink.release

install_requires = [
]

setuptools.setup(
    name='hii_plink',
    url='https://github.com/j2moreno/hii_plink',
    version=hii_plink.release.__version__,
    description='Tool that helps with a variety of plink commands',
    author='Leonardo Moreno',
    author_email='leo.moreno@epi.usf.edu',
    packages=[
        'hii_plink',
    ],
    entry_points={
        'console_scripts': [
            'hii_plink = hii_plink.cli:main',
        ]
    },
    install_requires=install_requires
)
