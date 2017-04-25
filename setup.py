import os
from setuptools import setup


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='chuck_pyutils',
    version='0.1',
    packages=['chuck_pyutils'],
    url='https://github.com/ChuckWoodraska/chuck-pyutils',
    license='',
    author='Chuck Woodraska',
    author_email='chuck.woodraska@gmail.com',
    description=read('README.md'),
    requires=[],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities"
    ]
)
