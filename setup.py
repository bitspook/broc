from setuptools import setup, find_packages

try:
    long_description = open("README.rst").read()
except IOError:
    long_description = ""

setup(
    name="broc",
    version="0.1.0",
    description="Broc: the brownie coder. Code for brownie points",
    license="MIT",
    author="Charanjit Singh",
    author_email="ckhabra@gmail.com",
    packages=find_packages(),
    install_requires=[],
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
    ]
)
