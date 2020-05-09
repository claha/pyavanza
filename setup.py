"""Setup script for pyavanza."""
import setuptools

setuptools.setup(
    name="pyavanza",
    version="0.1.0",
    author="Claes Hallstrom",
    author_email="hallstrom.claes@gmail.com",
    description="A Python wrapper around the Avanza mobile API",
    license="MIT License",
    url="https://github.com/claha/pyavanza",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
