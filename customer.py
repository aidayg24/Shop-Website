import csv
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import hashlib
import logging

LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename="logfile.log",
                    level=logging.DEBUG,
                    format=LOG_FORMAT,
                    filemode='a')

logger = logging.getLogger()

class Customer:
    def __init__(self):
        self.basket=[]

    def about(self):
        messagebox.showinfo("about maktab store",
                            "Project 4: Store Accounting\nprogramming by:\ntahere zare(raha),aida rostami,malihe mirzaii")

    def search(self):
        charge = Toplevel()
        charge.menubar = Menu(charge)
        charge.helpmenu = Menu(charge.menubar, tearoff=0)
        charge.helpmenu.add_command(label="About", command=self.about)
        charge.menubar.add_cascade(label="Help", menu=charge.helpmenu)
        charge.config(menu=charge.menubar)  # display the menu
        charge.scrollbar = Scrollbar(charge).grid(row=0, column=0, sticky="nes")
        charge.rowconfigure(0, minsize=800, weight=1)
        charge.columnconfigure(1, minsize=800, weight=1)
        taskbar_frame = Frame(charge, relief=RAISED, bd=2, bg='grey')
        btn_exit = Button(taskbar_frame, text="Exit", bg='red4', command=charge.quit).grid(row=10,
                                                                                            column=0, sticky="ew",
                                                                                            padx=5)
        ###***what is btn_exit?? you did not use this in the rest of program!
        taskbar_frame.grid(row=0, column=0, sticky="ns")
        """this method search in shop for the product that
         customer wants by giving the category and brand
         and return the price of the product"""
        file = open("product.csv", 'r')
        for line in file.readlines():
            data = line.strip().split(",")
            if data[0] == category and data[1] == brand:
                detail = "category:" + str(category) + " brand:" + str(brand) + "\n" + "price:" + data[3]
                return detail
            else:
                return "this product does not exist"

    def add_to_basket(self):
        pass
    def buy(self, basket):
        """the customer selects an item to buy and add that to the basket """
        pass

    def remove(self, basket):
        """the customer can remove an item from the basket before he or she get the final invoice"""
        pass

    def the_invoice(self, invoice, price):
        """this method records the final items in basket and gives an invoice and the price to
        customer and updates the entrepot """
        pass
