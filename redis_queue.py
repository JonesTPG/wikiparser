#!/usr/bin/env python3


import logging
import os
import config
import calculate_with_redis

from redis import Redis

from rq import Queue



logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger('requests').setLevel(logging.CRITICAL)
logger = logging.getLogger(__name__)


def main():
    pages = config.titlelist


    q = Queue(connection=Redis(host='localhost', port=6379))
    for i in range(0, config.GLOBAL_PAGE_AMOUNT):
        print("placed to queue")
        q.enqueue(calculate_with_redis.main, pages[i], pages[i+1])


if __name__ == '__main__':
    main()
