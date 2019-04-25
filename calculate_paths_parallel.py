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


# module that calculates the shortest path for the given pages
# the multiple_threads.py will run this module and calculate paths simultaneously


def main(source, target, database):

    ts = time()

    # Look up the IDs for each page
    try:
        (source_page_id, source_page_title,
         is_source_redirected) = database.fetch_page(source)
    except ValueError:
        raise InvalidRequest(
            'Start page "{0}" does not exist. Please try another search.'.format(
                source.encode('utf-8')))

    try:
        (target_page_id, target_page_title,
         is_target_redirected) = database.fetch_page(target)
    except ValueError:
        raise InvalidRequest(
            'End page "{0}" does not exist. Please try another search.'.format(target.encode('utf-8')))

    logging.info('Took %s seconds', time() - ts)

    paths = database.compute_shortest_paths(source_page_id, target_page_id)

    # No paths found
    if len(paths) == 0:
        logging.warn('No paths found from {0} to {1}'.format(source_page_id, target_page_id))

    # Paths found
    else:

        for path in paths:
            titlepath = ""
            for pageid in path:
                pagetitle = database.getName(pageid);
                titlepath = titlepath + " ** " + str(pagetitle[0])

            #the multi-threaded version can't use the function below, because the database cannot handle simultaneous
            #write operations...

            #database.save_result(source_page_id, source_page_title, target_page_id, target_page_title, len(path),
                                #titlepath)
        return len(paths)



