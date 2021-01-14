from knotprot_download import get_proteins, setup_download_dir, download_link, time_it
from functools import partial
from multiprocessing.pool import Pool
from threading import Thread
from queue import Queue

def run_sequentially(mydir):
    for p in get_proteins():
        download_link(mydir, p)

def run_multi_thread(dir):
    proteins = get_proteins()
    download = partial(download_link, dir)
    with Pool(4) as pl:
        pl.map(download, proteins)

class DownloadWorker(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            dir, prot = self.queue.get()
            #print('Worker got to download: ' + str(prot))
            try:
                download_link(dir, prot)
            finally:
                self.queue.task_done()

def run_workers(dir):
    proteins = get_proteins()
    queue = Queue()
    for n in range(10):
        worker = DownloadWorker(queue)
        worker.daemon = True
        worker.start()
    for p in proteins:
        queue.put((dir, p))
    queue.join()



mydir = setup_download_dir()
#print(get_proteins())
#time_it(run_sequentially, mydir)
#run_sequentially(mydir)
#time_it(run_multi_thread, mydir)
time_it(run_workers, mydir)
