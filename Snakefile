shell.prefix("export PATH=/ebio/abt3_projects/methanogen_host_evo/anaconda2/bin:$PATH;")

rule jupyter_exe:
    input:
        "notebooks/phenotype_explore.ipynb",
        "/ebio/abt3_projects/methanogen_host_evo/tmp/snkmk_test/data/pheno_phenotypes.txt"
    output:
        "/ebio/abt3_projects/methanogen_host_evo/tmp/snkmk_test/data/phenotype_summary//category_summary.pdf"
    shell:
        "source activate py3_ley0.2; "
        "jupyter nbconvert --to notebook --execute notebooks/phenotype_explore.ipynb --ExecutePreprocessor.kernel_name=python"
