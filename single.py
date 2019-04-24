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

#this program executes with no distribution whatsoever

def main():
    ts = time()

    print("Single thread calculation...")

    # Connect to the SDOW database and the results database.
    database = Database(sdow_database='./sdow.sqlite', searches_database='./result.sqlite')

    counter = 0

    for i in range(0,config.GLOBAL_PAGE_AMOUNT):

        source = config.titlelist[i]
        target = config.titlelist[i+1]

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

        #Paths found
        else:

            titlepath = "";



            for path in paths:
                #print("PATH FROM " + source + " TO " + target)

                counter=counter+1

                print("paths processed: " + str(counter))


                for pageid in path:
                    pagetitle = database.getName(pageid);
                    titlepath = titlepath + " ** " + str(pagetitle[0])
                    #print("page id: "  + str(pageid) + ": " + str(pagetitle[0]))
                #print("\n\n")

                database.save_result(source_page_id, source_page_title, target_page_id, target_page_title, len(path), titlepath)
                #print(titlepath)







if __name__ == '__main__':
    main()