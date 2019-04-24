from tkinter import *
from database import Database

import single




class UI:

    database = Database(sdow_database='./sdow.sqlite', searches_database='./result.sqlite')

    def __init__(self):
        self.__main_window = Tk()
        self.__main_window.geometry("600x600")

        self.__headertext = Label(self.__main_window, text="Wikiparser v2")
        self.__headertext.pack()

        self.__run_single_button= Button(self.__main_window, text="Run system with single worker (thread)",
                                   command=self.runsingle)
        self.__run_single_button.pack()

        self.__run_multiple_threads_button = Button(self.__main_window, text="Run system with multiple workers (8 threads)",
                                          command=self.runthreads)
        self.__run_multiple_threads_button.pack()

        self.__run_with_redis = Button(self.__main_window, text="Run system with redis queue (under development)",
                                                    command=self.runwithredis)
        self.__run_with_redis.pack()

        self._cleanbutton= Button(self.__main_window, text="Clean result database",
                                   command=self.cleandb)
        self._cleanbutton.pack()

        self.__exitbutton = Button(self.__main_window, text="Exit program",
                            command=self.exit)
        self.__exitbutton.pack()

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
        self.updateInfoText("running with 8 threads.")

    def runwithredis(self):
        self.updateInfoText("running with redis queue")

    def updateInfoText(self, newText):
        self.__infotext['text'] = newText

