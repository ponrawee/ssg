#! /usr/bin/env python

"""
Thai syllable segmentation using Conditional Random Fields
"""

from setuptools import setup

setup(
    name="ssg",
    packages=["ssg"],
    package_dir={"ssg": "ssg"},
    package_data={"ssg": ["artifacts/*"]},
    scripts=["scripts/ssg-cli"],
    include_package_data=True,
    version="0.0.3",
    install_requires=[
        'fire==0.2.1',
        'python-crfsuite==0.9.6',
        'tqdm==4.35.0'
    ],
    description="Thai syllable segmentation using Conditional Random Fields",
    author="Ponrawee Prasertsom",
    author_email="ponrawee.pra@gmail.com",
    url="https://github.com/ponrawee/ssg",
    download_url="https://github.com/ponrawee/ssg.git",
    keywords=["crf", "syllable", "tokenization", "thai"],
    classifiers=[
        "Development Status :: 3 - Alpha"
    ],
)
