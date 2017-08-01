"""Run jupyter notebooks with set parameters"""

import os

import nbformat
import nbparameterise

from nbconvert.preprocessors import ExecutePreprocessor

def run_notebook(notebook, new_notebook, params_dict, savedir, execute_nb=True):
    """
    Generate and run a notebook given existing notebook and dataset parameters

    Args:
        notebook (str): File name of original notebook
        new_notebook (str): File name of new notebook
        params_dict (dict): Dictionary containing name, delimiter, and composition column label for data file
        savedir (str): directory in which to save new notebook
        execute_nb (bool): Executes notebooks if True, otherwise only creates them
    """
    
    with open(notebook) as f:
        nb_run = nbformat.read(f, as_version=4)

    old_params = nbparameterise.extract_parameters(nb_run)
    params = nbparameterise.parameter_values(old_params, **params_dict)
    new_nb = nbparameterise.replace_definitions(nb_run, params, execute=False)

    cwd = os.getcwd()

    if execute_nb:
        ExecutePreprocessor(timeout=-1, kernel_name="python2").preprocess(new_nb, {"metadata":{"path":cwd}})

    if not os.path.isdir(savedir):
        os.mkdir(savedir)

    os.chdir(savedir)

    with open(new_notebook, mode='wt') as f:
        nbformat.write(new_nb, f)

    os.chdir(cwd)

if __name__=="__main__":

    #Dataset benchmarks
    deml_data = {"training_file":"datasets/deml_dataset.csv", "delimiter":',', "comp_col":"composition"} 
    meredig_data = {"training_file":"datasets/meredig_full.data", "delimiter":' ', "comp_col":"composition"}
    oqmd_data = {"training_file":"datasets/oqmd_all.data", "delimiter":' ', "comp_col":"comp"}

    datasets = [deml_data, meredig_data, oqmd_data]
    notebooks = ["Meredig_replication.ipynb", "Deml_descriptors.ipynb", "deJong_comp_descriptors.ipynb"]

    for nb in notebooks:
        for ds in datasets:
            ds_name = ds["training_file"][9:13]
            run_notebook(nb, "%s_%s"%(ds_name, nb), ds, "cross_benchmark")
