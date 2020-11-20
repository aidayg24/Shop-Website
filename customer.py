import csv
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import hashlib
import logging
from admin import Admin
admin=Admin()
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

    def add_to_basket(self):
        addtobaskt = Toplevel()
        addtobaskt.menubar = Menu(addtobaskt)
        addtobaskt.helpmenu = Menu(addtobaskt.menubar, tearoff=0)
        addtobaskt.helpmenu.add_command(label="About", command=self.about)
        addtobaskt.menubar.add_cascade(label="Help", menu=addtobaskt.helpmenu)
        addtobaskt.config(menu=addtobaskt.menubar)  # display the menu

        addtobaskt.rowconfigure(0, minsize=800, weight=1)
        addtobaskt.columnconfigure(1, minsize=800, weight=1)
        taskbar_frame = Frame(addtobaskt, relief=RAISED, bd=2, bg='grey')
        btn_admin = Button(taskbar_frame, text='Admin', bg='firebrick4', command=admin.login).grid(row=0, column=0,
                                                                                                   sticky="ew", padx=5,
                                                                                                   pady=5)
        btn_cart = Button(taskbar_frame, text='basket', bg='VioletRed4',command=self.showbasket).grid(row=2, column=0, sticky="ew", padx=5,
                                                                            pady=5)
        btn_exit = Button(taskbar_frame, text="Exit", bg='red4', command=addtobaskt.quit).grid(row=10, column=0, sticky="ew",
                                                                                          padx=5)
        taskbar_frame.grid(row=0, column=0, sticky="ns")

        fr_main = Frame(addtobaskt, relief=RAISED, bd=1)
        self.product_name = Entry(fr_main, width=30)
        self.brand = Entry(fr_main, width=30)
        self.number = Spinbox(fr_main, from_=0, to=100)
        add_btn = Button(fr_main, text='Add to basket', command=self.added).grid(row=7, column=1, padx=100, pady=6)
        lbl_product_name = ttk.Label(fr_main, text="product name : ").grid(row=2, column=0)
        lbl_brand = ttk.Label(fr_main, text="brand : ").grid(row=3, column=0)
        self.product_name.grid(row=2, column=1, sticky=W)
        self.brand.grid(row=3, column=1, sticky=W)
        self.number.grid(row=4, column=1, sticky=W)
        fr_main.grid(row=0, column=1, sticky="nsew")

        addtobaskt.mainloop()
    def added(self):
        file = open("product.csv", 'r')
        for line in file.readlines():
            data = line.strip().split(",")
            if self.product_name.get() == data[0] and self.brand.get() == data[1]:
                num = int(self.number.get())
                if int(self.number.get())<int(data[4]):
                    self.basket.append((data[0],data[1],data[3],num))
                    messagebox.showinfo('Buy','Product added to your basket')
                    logger.info('An item was added to a customers basket')

                else:
                    messagebox.showerror('Buy', 'The amount you want is more than the inventory')
                    logger.error('Unsuccessful attempt to buy goods')

    def showbasket(self):
        baskett=Toplevel()
        baskett.menubar = Menu(baskett)
        baskett.helpmenu = Menu(baskett.menubar, tearoff=0)
        baskett.helpmenu.add_command(label="About", command=self.about)
        baskett.menubar.add_cascade(label="Help", menu=baskett.helpmenu)
        baskett.config(menu=baskett.menubar)  # display the menu

        baskett.rowconfigure(0, minsize=800, weight=1)
        baskett.columnconfigure(1, minsize=800, weight=1)
        taskbar_frame = Frame(baskett, relief=RAISED, bd=2, bg='grey')
        btn_admin = Button(taskbar_frame, text='Admin', bg='firebrick4', command=admin.login).grid(row=0, column=0,
                                                                                                   sticky="ew", padx=5,
                                                                                                   pady=5)
        btn_cart = Button(taskbar_frame, text='basket', bg='VioletRed4',command=self.showbasket).grid(row=2, column=0, sticky="ew", padx=5,
                                                                            pady=5)
        btn_exit = Button(taskbar_frame, text="Exit", bg='red4', command=baskett.quit).grid(row=10, column=0, sticky="ew",
                                                                                          padx=5)
        taskbar_frame.grid(row=0, column=0, sticky="ns")

        fr_main = Frame(baskett, relief=RAISED, bd=1)
        producnamebrand = Label(fr_main, text='info',bg='tomato4')
        price = Label(fr_main, text='price of one',bg='tomato4')
        number = Label(fr_main, text='counter',bg='tomato4')
        sum = Label(fr_main, text='sum',bg='tomato4')
        producnamebrand.grid(row=0, column=0, sticky="w", padx=5, pady=5)
        number.grid(row=0, column=1, sticky="w", padx=5, pady=5)
        price.grid(row=0, column=2, sticky="w", padx=5, pady=5)
        sum.grid(row=0, column=3, sticky="w", padx=5, pady=5)
        row=2
        totallsum=0
        for product in self.basket:
            producnamebrand = Label(fr_main, text=product[0]+','+product[1])
            price = Label(fr_main, text=product[2])
            number = Label(fr_main,text=product[3])
            totallsum += int(product[2])*int(product[3])
            sum = Label(fr_main,text=str(int(product[2])*int(product[3])))
            producnamebrand.grid(row=row, column=0, sticky="w", padx=5, pady=5)
            number.grid(row=row, column=1, sticky="w", padx=5, pady=5)
            price.grid(row=row, column=2, sticky="w", padx=5, pady=5)
            sum.grid(row=row, column=3, sticky="w", padx=5, pady=5)
            row += 1
        totall= Label(fr_main,text='totall sum = '+str(totallsum))
        totall.grid(row=row, column=3, sticky="w", padx=5, pady=5)
        buy_btn = Button(fr_main, text="Click if you want your purchase to be final", bg='red4', command=self.buy)
        buy_btn.grid(row=row+1,sticky="w", padx=5, pady=5)
        fr_main.grid(row=0, column=1, sticky="nsew")
        baskett.mainloop()
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
