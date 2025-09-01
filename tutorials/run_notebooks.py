import os
import shutil

html_dir = os.path.abspath(os.path.join("..", "docs"))

cwd = os.getcwd()

clear = False
pdf = False
html = False
allow_errors = True

def run_nb(nb_file, nb_dir="."): 
    os.chdir(nb_dir)
    worker_dirs = [d for d in os.listdir(".") if os.path.isdir(d) and d.startswith("worker")]
    for worker_dir in worker_dirs:
        shutil.rmtree(worker_dir)
    if allow_errors:
        os.system("jupyter nbconvert --execute --ExecutePreprocessor.timeout=180000 --allow-errors --inplace {0}".format(nb_file))
    else:
        os.system("jupyter nbconvert --execute --ExecutePreprocessor.timeout=180000 --inplace {0}".format(nb_file))
    if html:
        os.system("jupyter nbconvert --to html {0}".format(nb_file))
        md_file = nb_file.replace('.ipynb', '.html')
        shutil.move(md_file, os.path.join(html_dir, md_file))
        print('preped htmlfile: ', os.path.join(html_dir, md_file))
    if pdf:
        os.system("jupyter nbconvert --to pdf {0}".format(nb_file))
    if clear:
        os.system("jupyter nbconvert --ClearOutputPreprocessor.enabled=True --ClearMetadataPreprocessor.enabled=True --allow-errors --inplace {0}".format(nb_file))
    os.chdir(cwd)
    return

nb_dir = "."
nb_file = "01_pstfrom.ipynb"
run_nb(nb_file, nb_dir)


nb_file = "02_prior_mc_and_truth.ipynb"
run_nb(nb_file, nb_dir)

nb_file = "03_ies_part1.ipynb"
run_nb(nb_file, nb_dir)

nb_file = "04_opt.ipynb"
run_nb(nb_file, nb_dir)

