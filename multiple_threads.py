import logging
import os
from time import time
from database import Database
from threading import Thread
from queue import Queue

import calculate_paths


import config

try:
    from sets import Set
except ImportError:
    Set = set

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

counter = 0


# Connect to the SDOW database and the results database.
database1 = config.THREAD_1_DATABASE_CON
database2 = config.THREAD_2_DATABASE_CON
database3 = config.THREAD_3_DATABASE_CON
database4 = config.THREAD_4_DATABASE_CON

databaselist = [database1, database2, database3, database4]
# a class for the worker (extends the python Thread-class)

class WikiparserWorker(Thread):

    def __init__(self, queue, database):
        Thread.__init__(self)
        self.queue = queue
        self.database = database

    def run(self):
        global counter
        while True:
            pages = self.queue.get()
            try:
                pathamount = calculate_paths.main(pages[0], pages[1], self.database)

                oldcounter = counter
                # catch the possible type error in the case of no paths found between wikipedia pages
                try:
                    counter = counter + pathamount

                except TypeError:
                    counter = oldcounter
                finally:
                    print("paths processed: " + str(counter))

            finally:
                self.queue.task_done()



#this program executes with 8 threads


def main():

    global counter
    counter = 0
    ts = time()

    print("Setting up multiple workers...")



    # create a queue to communicate with the worker threads
    queue = Queue()


    # create 4 worker threads
    for x in range(4):
        #each of the worker gets its own database, so that they can work simultaneously
        worker = WikiparserWorker(queue, databaselist[x])
        # Setting daemon to True will let the main thread exit even though the workers are blocking
        worker.daemon = True
        worker.start()
        # Put the pages to the queue as a tuple

    for i in range(0, config.GLOBAL_PAGE_AMOUNT):
        source = config.titlelist[i]
        target = config.titlelist[i + 1]
        queue.put((source, target))

    #causes the main thread to wait for the queue to finish processing all the tasks
    queue.join()
    logging.info('Took %s', time() - ts)

    print("time elapsed: " + str(time() - ts) + " seconds")
    print("paths calculated: " + str(counter))
    print("average time/path:" + str((time() - ts) / counter))





if __name__ == '__main__':
    main()
