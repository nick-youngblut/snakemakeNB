#!/usr/bin/env python

from __future__ import print_function

import os
import sys
import re
import shlex
import json
import nbformat


class NB_Extractor:
    def __init__(self, nb_files, conda=None):
        self.nb_files = nb_files
        self.conda = conda
        
    def to_snakefile(self):
        # activate
        if self.conda:
            print('conda_env = "{}"\n'.format(self.conda))
        # snakemake rul
        for F in self.nb_files:
            nbe = _NB_Extractor(F)
            nbe.extract()
            nbe.to_snakefile()
        

class _NB_Extractor():
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
        rex_space = re.compile('\s+') 
        rex_split = re.compile('\s*=\s*')
        for i in range(len(code)):
            if rex_input.match(code[i]):
                # parsing comment
                comm = re.split(rex_input, code[i], maxsplit=1)
                x = re.split(rex_space, comm[1], maxsplit=1)
                sm_grammar = x[0].lower()
                try: 
                    comm_params = shlex.split(x[1])
                except IndexError:
                    comm_params = []
                # appending params & values
                if sm_grammar in ('input','output'):
                    # parsing next line 
                    comm_params = re.split(rex_split, code[i+1], maxsplit=1)
                    try:
                        self.sm_params[sm_grammar].append(comm_params[1])
                    except KeyError:
                        self.sm_params[sm_grammar] = [comm_params[1]]
                elif sm_grammar in ('params'):
                    # parsing params from comment
                    for x in comm_params:
                        k,v = re.split(rex_split, x, maxsplit=1)
                        v = '"{}"'.format(v)
                        try:
                            self.sm_params[sm_grammar][k] = v
                        except KeyError:
                            self.sm_params[sm_grammar] = {k:v}
                elif sm_grammar in ('message'):
                    comm_params = ['"{}"'.format(x) for x in comm_params]
                    self.sm_params[sm_grammar] = comm_params
                else:
                    self.sm_params[sm_grammar] = comm_params
                        
    def to_json(self):
        json.dump(self.sm_params, sys.stdout)

    def to_snakefile(self, sp='    '):
        """
        sp = spacing 
        """
        # rule header
        print('rule {}_run:'.format(self.sm_rule))
        # rule params 
        for pp in self.sm_psbl_params:
            try:
                params = self.sm_params[pp]
            except KeyError:
                continue
            # snakemake grammer header
            print('{}{}:'.format(sp, pp))
            # values for snakemake grammer
            try:
                j = []
                for k,v in params.items():
                    j.append('{}{}={}'.format(sp*2, k, v))
                print(',\n'.join(j))
            except AttributeError:
                j = ',\n'.join([sp*2+x for x in params])
                print(j)
                                    
        # shell
        try:
            x = self.sm_params['params']['conda_env']
            conda_env = 'params.conda_env'
        except KeyError:
            conda_env = 'conda_env'            
        print('{}shell:'.format(sp))        
        print('{}\'source activate {}; \''.format(sp*2, '{' + conda_env + '}'))
        print('{}\'jupyter nbconvert '
              '--to notebook --execute {} '
              ' --ExecutePreprocessor.kernel_name=python '
              '--inplace\''.format(sp*2, self.nb_file))
        print('')
        
        

if __name__ == '__main__':
    nb_file = '../notebooks/NB1.ipynb'
    nbe = NB_Extractor(nb_file, conda=None)
    nbe.to_snakefile()
