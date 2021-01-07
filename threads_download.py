from knotprot_download import get_proteins, setup_download_dir, download_link, time_it
from functools import partial
from multiprocessing.pool import Pool

def run_sequentially(mydir):
    for p in get_proteins():
        download_link(mydir, p)

def run_multi_thread(dir):
    proteins = get_proteins()
    download = partial(download_link, dir)
    with Pool(4) as pl:
        pl.map(download, proteins)

mydir = setup_download_dir()
#print(get_proteins())
#time_it(run_sequentially, mydir)
#run_sequentially(mydir)
time_it(run_multi_thread, mydir)
