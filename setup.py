from setuptools import setup, find_packages
import os
import snakemakeNB

VERSION = snakemakeNB.__version__

install_reqs = [
'ipython'
]

setup(
    name='snakemakeNB',
    version=VERSION,
    license='MIT',
    description=('Create snakemake rules to run Jupyter/Ipython Notebooks'),
    author='Nicholas Youngblut',
    author_email='nyoungb2@gmail.com',
    url='https://github.com/nick-youngblut/jupyterSM',
    packages=find_packages(exclude=[]),
    scripts=['bin/snakemake-nb.py'],
    install_requires=install_reqs,
    long_description="""
    Create snakemake rules to batch run Jupyter/Ipython Notebooks
    with snakemake.
    """
)
