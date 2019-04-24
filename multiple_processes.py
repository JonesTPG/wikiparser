import logging
import os
from functools import partial
from multiprocessing.pool import Pool
from time import time

import calculate_paths


import config

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger('requests').setLevel(logging.CRITICAL)
logger = logging.getLogger(__name__)


def main():


    pages = config.titlelist
    database = config.DATABASE_CON



    with Pool(4) as p:
        p.map(calculate_paths.main(), [])

if __name__ == '__main__':
    main()