import logging
import os
from time import time
from database import Database
from helpers import InvalidRequest, fetch_wikipedia_pages_info

import config

try:
    from sets import Set
except ImportError:
    Set = set





logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

#this program executes with 8 threads



def main():
    ts = time()

    print("Single thread calculation...")

    # Connect to the SDOW database and the results database.
    database = Database(sdow_database='./sdow.sqlite', searches_database='./result.sqlite')

    counter = 0







if __name__ == '__main__':
    main()
