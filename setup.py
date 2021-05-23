from setuptools import setup

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='dconnect',
    version='0.0.2',
    author="Nitesh Kumar",
    author_email="nit567esh@gmail.com",
    description="Power your data connections with python and queries with dconnect",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nit567esh/dconnect",
    packages=['dconnect'],
   install_requires=['pandas'], #external packages as dependencies
)