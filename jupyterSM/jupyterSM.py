#!/usr/bin/env python

from __future__ import print_function

import os
import sys
import re
import json
import nbformat


class NB_Extractor:
    def __init__(self, nb_file):
        self.nb_file = nb_file
        self.sm_rule = os.path.splitext(os.path.basename(nb_file))[0]
        self.sm_psbl_params = ('input', 'output', 'workdir', 
                               'message', 'threads', 'resources', 
                               'version', 'snakemake', 'rule', 'include', 
                               'ni', 'params', 'log', 'benchmark', 'run')
        self.sm_params = {'input': ["'{}'".format(self.nb_file)]}
        self.nb = nbformat.read(nb_file, nbformat.NO_CONVERT)

    def extract(self):
        for cell in self.nb['cells']:
            if cell['cell_type'] == 'code':
                self._parse_code(cell['source'])

    def _parse_code(self, code):
        """
        code = 'source' string from code cell
        """
        code = code.split('\n')
        rex_input = re.compile('\s*#\s*snakemake::\s*')
        rex_split = re.compile('\s*=\s*')
        for i in range(len(code)):
            if rex_input.match(code[i]):
                # parsing comment
                comm = re.split(rex_input, code[i], maxsplit=1)
                param = comm[1].lower()
                # parsing values 
                vals = re.split(rex_split, code[i+1], maxsplit=1)
                # adding to SM params
                try:
                    self.sm_params[param].append(vals[1])
                except KeyError:
                    self.sm_params[param] = [vals[1]]

    def to_json(self):
        json.dump(self.sm_params, sys.stdout)

    def to_snakefile(self, sp='    '):
        """
        sp = spacing 
        """
        # rule header
        print('rule {}_run:'.format(self.sm_rule))
        # rule params 
        for p in self.sm_psbl_params:
            try:
                ps = ',\n'.join([sp*2+x for x in self.sm_params[p]]) 
                print('{}{}:\n{}'.format(sp, p, ps))
            except KeyError:
                pass
        # shell
        print('{}shell:'.format(sp))
        print('{}\'{}\''.format(sp*2, '{activate}; '))
        print('{}\'jupyter nbconvert --to notebook --execute {} --ExecutePreprocessor.kernel_name=python\''.format(sp*2, self.nb_file))
        
        

if __name__ == '__main__':
    nb_file = '/ebio/abt3_projects/small_projects/nyoungblut/dev/jupyterSM/notebooks/NB1.ipynb'
    nbe = NB_Extractor(nb_file)
    nbe.extract()
    nbe.to_snakefile()
