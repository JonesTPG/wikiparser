#!/usr/bin/env python3

from tkinter import *
from database import Database

import single
import multiple_threads
import redis_queue
import config



class UI:

    database = config.DATABASE_CON

    def __init__(self):
        self.__main_window = Tk()
        self.__main_window.geometry("600x600")

        self.__main_window.title('Wikiparser v2')

        self.__run_single_button= Button(self.__main_window, text="Run system with single worker (thread)",
                                   command=self.runsingle)
        self.__run_single_button.pack()

        self.__emptytext = Label(self.__main_window, text="")
        self.__emptytext.pack()

        self.__run_multiple_threads_button = Button(self.__main_window, text="Run system with multiple workers (4 threads)",
                                          command=self.runthreads)
        self.__run_multiple_threads_button.pack()

        self.__emptytext2 = Label(self.__main_window, text="")
        self.__emptytext2.pack()

        #self.__run_multiple_processes_button = Button(self.__main_window,
                                                    #text="Run system with multiple workers (4 processes)",
                                                   # command=self.runprocesses)
        #self.__run_multiple_processes_button.pack()

        #self.__emptytext7 = Label(self.__main_window, text="")
        #self.__emptytext7.pack()


        self.__run_with_redis = Button(self.__main_window, text="Run system with redis queue (under development)",
                                                    command=self.runwithredis)
        self.__run_with_redis.pack()

        self.__emptytext3 = Label(self.__main_window, text="")
        self.__emptytext3.pack()

        self._cleanbutton= Button(self.__main_window, text="Clean result database",
                                   command=self.cleandb)
        self._cleanbutton.pack()

        self.__emptytext4 = Label(self.__main_window, text="")
        self.__emptytext4.pack()

        self._generatebutton = Button(self.__main_window, text="Generate new random pages",
                                   command=self.generatepages)
        self._generatebutton.pack()

        self.__emptytext12 = Label(self.__main_window, text="")
        self.__emptytext12.pack()

        self.__exitbutton = Button(self.__main_window, text="Exit program",
                            command=self.exit)
        self.__exitbutton.pack()

        self.__emptytext5 = Label(self.__main_window, text="")
        self.__emptytext5.pack()

        self.__infotext = Label(self.__main_window, text="Please choose an operation to be performed.")
        self.__infotext.pack()

        self.__main_window.mainloop()

    def exit(self):
        self.__main_window.destroy()
        exit(1)

    def cleandb(self):
        self.updateInfoText("cleaning database...")
        self.database.clean_results()
        self.updateInfoText("database cleaned.")


    def runsingle(self):
        self.updateInfoText("running on a single thread.")
        single.main()
        self.updateInfoText("program executed succesfully.")

    def runthreads(self):
        self.updateInfoText("running with 4 threads.")
        multiple_threads.main()
        self.updateInfoText("program executed succesfully.")

    def runprocesses(self):
        self.updateInfoText("running with 4 separate processes.")

        self.updateInfoText("program executed succesfully.")

    def generatepages(self):
        self.updateInfoText("Generating new random pages...")
        config.main()
        self.updateInfoText("New random pages generated.")

    def runwithredis(self):
        self.updateInfoText("running with redis queue")
        redis_queue.main()
        self.updateInfoText("program executed succesfully.")

    def updateInfoText(self, newText):
        self.__infotext['text'] = newText



