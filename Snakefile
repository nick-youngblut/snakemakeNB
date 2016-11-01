shell.prefix("export PATH=/ebio/abt3_projects/small_projects/nyoungblut/anaconda2/bin:$PATH;")

activate = "source activate py3_ley0.2"

rule NB1_run:
    input:
        '/ebio/abt3_projects/small_projects/nyoungblut/dev/jupyterSM/notebooks/NB1.ipynb',
        '/ebio/abt3_projects/small_projects/nyoungblut/dev/jupyterSM/data/mtcars.txt'
    output:
        '/ebio/abt3_projects/small_projects/nyoungblut/dev/jupyterSM/data/mtcars_n.txt'
    shell:
        '{activate}; '
        'jupyter nbconvert --to notebook --execute /ebio/abt3_projects/small_projects/nyoungblut/dev/jupyterSM/notebooks/NB1.ipynb --ExecutePreprocessor.kernel_name=python'

