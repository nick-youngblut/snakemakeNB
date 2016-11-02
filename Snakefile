rule NB2_run:
    input:
        'notebooks/NB2.ipynb',
        '/ebio/abt3_projects/small_projects/nyoungblut/dev/jupyterSM/data/mtcars_n.txt'
    output:
        '/ebio/abt3_projects/small_projects/nyoungblut/dev/jupyterSM/data/mtcars_n.pdf'
    params:
        conda_env='py3_ley0.2'
    shell:
        'source activate {params.conda_env}; '
        'jupyter nbconvert --to notebook --execute notebooks/NB2.ipynb  --ExecutePreprocessor.kernel_name=python --inplace'
