rule NB1_run:
    input:
        'notebooks/NB1.ipynb',
        '/ebio/abt3_projects/small_projects/nyoungblut/dev/jupyterSM/data/mtcars.txt'
    output:
        '/ebio/abt3_projects/small_projects/nyoungblut/dev/jupyterSM/data/mtcars_n.txt'
    params:
        conda_env="py3_ley0.2"
    shell:
        'source activate {params.conda_env}; '
        'jupyter nbconvert --to notebook --execute notebooks/NB1.ipynb  --ExecutePreprocessor.kernel_name=python --inplace'
rule NB2_run:
    input:
        'notebooks/NB2.ipynb',
        '/ebio/abt3_projects/small_projects/nyoungblut/dev/jupyterSM/data/mtcars_n.txt'
    output:
        '/ebio/abt3_projects/small_projects/nyoungblut/dev/jupyterSM/data/mtcars_n.pdf'
    message:
        "this is a message"
    params:
        conda_env="py3_ley0.2"
    shell:
        'source activate {params.conda_env}; '
        'jupyter nbconvert --to notebook --execute notebooks/NB2.ipynb  --ExecutePreprocessor.kernel_name=python --inplace'
