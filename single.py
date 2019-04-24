import logging
import os
from time import time
from database import Database
from helpers import InvalidRequest, fetch_wikipedia_pages_info

import config
import calculate_paths

try:
    from sets import Set
except ImportError:
    Set = set





logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

#this program executes with no distribution whatsoever

def main():
    ts = time()

    print("Single thread calculation...")

    # Connect to the SDOW database and the results database.
    database = config.DATABASE_CON

    counter = 0

    for i in range(0,config.GLOBAL_PAGE_AMOUNT):

        source = config.titlelist[i]
        target = config.titlelist[i+1]

        pathamount = calculate_paths.main(source, target, database)

        oldcounter = counter

        #catch the possible type error in the case of no paths found between wikipedia pages
        try:
            counter = counter + pathamount

        except TypeError:
            counter = oldcounter
        finally:
            print("paths processed: " + str(counter))



    print("time elapsed: " + str(time()-ts) + " seconds")
    print("paths calculated: " + str(counter))
    print("average time/path:" + str( (time()-ts) / counter ))



if __name__ == '__main__':
    main()