#!/usr/bin/env python

from __future__ import print_function

import os
import sys
import argparse

scriptDir = os.path.dirname(__file__)
libDir = os.path.join(scriptDir, 'jupyterSM')
sys.path.append(libDir)
from jupyterSM import jupyterSM


def parse_args():
    desc = 'Jupyter-snakemake'
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('files', metavar='file', type=str, nargs='+',
                        help='Notebook (.ipynb) file')
    parser.add_argument('-c', '--conda', type=str, default=None,
                        help='conda environment to source activate for all notebooks')
    args = parser.parse_args()
    return(args)


if __name__ == '__main__':
    args = parse_args()
    nbe = jupyterSM.NB_Extractor(args.files, args.conda)
    nbe.to_snakefile()    
