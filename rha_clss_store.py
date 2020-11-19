from tkinter import *  # importing tkinter library
from tkinter import messagebox


# inherianceing from Tk module and initializing the Tk class for creating object
class StoreWindow(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title('maktab store')
        self.minsize(500, 500)  # set the minimum size of window
        self.maxsize(1600, 1200)  # set the maximum size of window
        self.geometry('800x600')  # set the default window size when opens
        self.menubar = Menu(self)  # create a toplevel menu
        self.helpmenu = Menu(self.menubar, tearoff=0)  # create a pulldown menu, and add it to the menu bar
        self.helpmenu.add_command(label="About", command=self.about)
        self.menubar.add_cascade(label="Help", menu=self.helpmenu)
        self.config(menu=self.menubar)  # display the menu
        self.scrollbar = Scrollbar(self).grid(row=0, column=0, sticky="nes")

    def about(self):
        messagebox.showinfo("about maktab store",
                            "Project 4: Store Accounting\nprogramming by:\ntahere zare(raha),aida rostami,malihe mirzaii")