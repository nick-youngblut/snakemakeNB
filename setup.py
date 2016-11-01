from setuptools import setup, find_packages
import os
import jupyterSM

VERSION = jupyterSM.__version__

install_reqs = [
'ipython'
]

setup(
    name='jupyterSM',
    version=VERSION,
    license='MIT',
    description=('')
    author='Nicholas Youngblut',
    author_email='nyoungb2@gmail.com',
    url='https://github.com/nick-youngblut/jupyterSM',
    packages=find_packages(exclude=[]),
    install_requires=install_reqs,
    long_description="""
    """
)
