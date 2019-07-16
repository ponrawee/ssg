#! /usr/bin/env python

"""
Thai syllable segmentation using Conditional Random Field
"""

from setuptools import setup

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="ssg",
    packages=["ssg"],
    package_dir={"ssg": "ssg"},
    package_data={"ssg": ["artifacts/*"]},
    scripts=["scripts/ssg-cli"],
    include_package_data=True,
    version="0.0.1",
    install_requires=requirements,
    license="MIT",
    description="Thai syllable segmentation using Conditional Random Field",
    author="Ponrawee Prasertsom",
    author_email="ponrawee.pra@gmail.com",
    url="https://github.com/ponrawee/ssg",
    download_url="https://github.com/ponrawee/ssg.git",
    keywords=["crf", "syllable", "tokenization", "thai"],
    classifiers=[
        "Development Status :: 3 - Alpha"
    ],
)