#!/usr/bin/env python3

from ui import UI

import config



def main():

    #lets run the config.py so that we get the list that contains 500 random wiki pages

    print("fetching random pages...")

    config.main()

    print("pages fetched.")

    #lets fire up the USER INTERFACE

    print("starting user interface...")

    ui = UI()





if __name__ == '__main__':
    main()