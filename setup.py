"""Setup script for pyavanza."""
from setuptools import find_packages, setup

NAME = "pyavanza"
VERSION = "0.2.0"
LICENSE = "MIT License"
AUTHOR = "Claes Hallstrom"
URL = "https://github.com/claha/pyavanza"
EMAIL = "hallstrom.claes@gmail.com"

DESCRIPTION = "A Python wrapper around the Avanza mobile API"

PACKAGES = find_packages()

REQUIRES = [
    "aiohttp>=3.6.1",
]

CLASSIFIERS = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
]

setup(
    name=NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=EMAIL,
    description=DESCRIPTION,
    license=LICENSE,
    url=URL,
    packages=PACKAGES,
    install_requires=REQUIRES,
    classifiers=CLASSIFIERS,
)
