#!/usr/bin/env python

from Tkinter import *

class Application(Frame):
    """buid the basec window frame template"""

    def __init__(self,master):
        Frame .__init__(self,master)
        self.grid()

root=Tk()
root.title("this is my fist GUI")
root.geometry('300x500')
app = Application(root)
app.mainloop()
