import os
import shutil
import platform
import flopy
import pandas as pd
import numpy as np

def test_extract_hds_arrays(d):
    """
    Test the extraction of head data arrays.
    """
    cwd = os.getcwd()
    os.chdir(d)
    extract_hds_arrays_and_list_dfs()
    os.chdir(cwd)

def process_secondary_obs(ws='.'):
    """
    Process secondary observation files.
    """
    def write_tdif_obs(orgf, newf, ws='.'):
        df = pd.read_csv(os.path.join(ws,orgf), index_col='time')
        df = df - df.iloc[0, :]
        df.to_csv(os.path.join(ws,newf))
        return

    # write the tdiff observation csv's
    write_tdif_obs('model.obs.head.pit.csv', 'heads.tdiff.csv', ws)

    print('Secondary observation files processed.')
    return

def extract_hds_arrays_and_list_dfs():
    """
    Extract head data arrays and list budget dataframes from MODFLOW output files.
    """

    hds = flopy.utils.HeadFile("model.hds")
    for it,t in enumerate(hds.get_times()):
        d = hds.get_data(totim=t)
        for k,dlay in enumerate(d):
            np.savetxt("hdslay{0}_t{1}.txt".format(k+1,it+1),d[k,:,:],fmt="%15.6E")

    lst = flopy.utils.Mf6ListBudget("model.lst")
    inc,cum = lst.get_dataframes(diff=True,start_datetime=None)
    inc.columns = inc.columns.map(lambda x: x.lower().replace("_","-"))
    cum.columns = cum.columns.map(lambda x: x.lower().replace("_", "-"))
    inc.index.name = "totim"
    cum.index.name = "totim"
    #one lil trick to help with opt later
    rd = pd.read_csv("dewater.autoreduce.csv")
    summed = rd.groupby("time").sum()["wel-reduction"].to_dict()
    inc["abstotwel"] = np.abs(inc["wel"]) + np.abs(inc["wel2"])
    cum["abstotwel"] = np.abs(cum["wel"]) + np.abs(cum["wel2"])
    inc["totwel"] = inc["wel"] + inc["wel2"]
    cum["totwel"] = cum["wel"] + cum["wel2"]
    inc["wel-reduction"] = 0.0
    for t,v in summed.items():
        inc.loc[t,"wel-reduction"] = v
    inc.to_csv("inc.csv")
    cum.to_csv("cum.csv")


    return

def prep_bins(dest_path):
    """
    Prepare binary files for the specified destination path and OS.
    """
    if "linux" in platform.platform().lower():
        bin_path = os.path.join("..", "bin", "linux")
    elif "darwin" in platform.platform().lower() or "macos" in platform.platform().lower():
        bin_path = os.path.join("..", "bin", "mac")
    else:
        bin_path = os.path.join("..", "bin", "win")
    files = os.listdir(bin_path)
    for f in files:
        if os.path.exists(os.path.join(dest_path,f)):
            os.remove(os.path.join(dest_path,f))
        shutil.copy2(os.path.join(bin_path,f),os.path.join(dest_path,f))

def dir_cleancopy(org_d, new_d, delete_orgdir=False):
    """
    Clean and copy directory.
    """
    # remove existing folder
    if os.path.exists(new_d):
        shutil.rmtree(new_d)
    # copy the original model folder across
    shutil.copytree(org_d, new_d)
    print(f'Files copied from:{org_d}\nFiles copied to:{new_d}')

    if delete_orgdir==True:
        shutil.rmtree(org_d)
        print(f'Hope you did that on purpose. {org_d} has been deleted.')
    #prep_bins(new_d)
    return

