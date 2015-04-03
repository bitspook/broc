from setuptools import setup, find_packages

try:
    long_description = open("README.rst").read()
except IOError:
    long_description = ""

setup(
    name="broc",
    version="0.1.3",
    description="Broc: the brownie coder. Code for brownie points",
    license="MIT",
    author="Charanjit Singh",
    author_email="ckhabra@gmail.com",
    packages=['broc', 'broc.git-hooks'],
    install_requires=[
        'Click',
        'shell'
    ],
    entry_points='''
        [console_scripts]
        broc=broc:cli
    ''',
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
    ]
)
