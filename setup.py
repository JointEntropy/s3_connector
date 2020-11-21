
"""
Установщик пакета
"""

import setuptools
from setuptools import find_packages


with open("README.md") as fh:
    long_description = fh.read()

requires = open('requirements.txt').read().split('\n')


setuptools.setup(
    name="connectors",
    version="0.0.3",  # engine version . number of api methods . number of fixes in version
    author="Grigory Ovchinnikov",
    author_email="ogowm@hotmail.com",
    description="Connectors utils",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JointEntropy/s3_connector",
    packages=find_packages(),
    install_requires=requires,
    setup_requires=[
        'pytest-runner',
    ]
)