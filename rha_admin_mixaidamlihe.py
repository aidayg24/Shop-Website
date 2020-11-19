import csv
from rha_clss_store import StoreWindow
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


class Admin:
    def __init__(self):
        file = open("admin info.txt", "r")
        password = file.readline().split(",")
        self.password = str(password[1])  # the password by default is 0000
        self.logging_counter = True

    def login(self):
        getpass = StoreWindow()
        getpass.rowconfigure(0, minsize=800, weight=1)
        getpass.columnconfigure(1, minsize=800, weight=1)
        taskbar_frame = Frame(getpass, relief=RAISED, bd=2, bg='grey')
        btn_exit = Button(taskbar_frame, text="Exit", bg='red4', command=getpass.quit).grid(row=10,
                                                                                            column=0, sticky="ew",
                                                                                            padx=5)
        taskbar_frame.grid(row=0, column=0, sticky="ns")

        fr_main = Frame(getpass, relief=RAISED, bd=1)
        pas = Entry(fr_main, width=30).config(show='*')
        log_btn = Button(fr_main, text='Login', command=self.chekpassword).grid(row=3, column=1, padx=100, pady=6)
        lbl_pas = ttk.Label(fr_main, text="Your Password : ").grid(row=2, column=0)
        entry_password = str(pas.get()).encode()
        self.hash_entry_password = hashlib.md5(entry_password).hexdigest()

    def chekpassword(self):
        if self.hash_entry_password == self.password:
            logging = StoreWindow()
            logger.info("admin log in!")
            logging.rowconfigure(0, minsize=800, weight=1)
            logging.columnconfigure(1, minsize=800, weight=1)
            taskbar_frame = Frame(logging, relief=RAISED, bd=2, bg='grey')
            btn_add = Button(taskbar_frame, text='New Product', bg='VioletRed4', command=self.add_new_product()).grid(
                row=0, column=0, sticky="ew", padx=5, pady=5)
            btn_invoice = Button(taskbar_frame, text='Invoices', bg='VioletRed4', command=self.show_invoices()).grid(
                row=1, column=0, sticky="ew", padx=5, pady=5)
            btn_change_password = Button(taskbar_frame, text='Change Password', bg='VioletRed4',
                                         command=self.change_info()).grid(row=2, column=0, sticky="ew", padx=5, pady=5)
            btn_exit = Button(taskbar_frame, text="Exit", bg='red4', command=logging.quit).grid(row=10, column=0,
                                                                                                sticky="ew", padx=5)
            taskbar_frame.grid(row=0, column=0, sticky="ns")

            fr_main = Frame(logging, relief=RAISED, bd=1)
            file = open("product.csv", 'r')
            mylist = Listbox(fr_main, yscrollcommand=logging.scrollbar.set)
            for line in file.readlines():
                data = line.strip().split(",")
                show = "category: " + data[0] + " brand: " + data[1] + " barcode: " + data[2] + " price: " + data[
                    3] + " stock: " + data[4]
                mylist.insert(END, str(show))
            mylist.grid(row=2, column=0, sticky="ew", padx=5, pady=5)

            if self.logging_counter:
                logger.warning("First login: insecure password")
                messagebox.showwarning("Security and privacy", "Please change your password first")
                self.logging_counter = False
            ###in main : print("login was successful.")
            ###in main :log.info("admin log in!")
            return True
        else:
            ###in main :print("your password or user name was not correct")
            ###in main we can manage if the password is wrong or the user name
            ###in main :log.warning("login failed")
            return False

    def change_info(self, user, pas):
        """the admin can change the user name and password"""
        ###we must have an item in main to change info !
        file = open(file_path, "w+")
        self.name = user
        self.password = pas
        file.write("user name ," + str(self.name) + ", password," + str(self.password))
        file.close()
        ###in main:log.info:"change info successfully"
        return "the information successfully changed"

    def add_new_product(self, product_name, brand, barcode, price, stock):
        """admin can add new product to the list of products and updates the entrepot"""
        with open('product.csv', 'a', newline='') as csvpr:
            fieldnames = ['product name', 'brand', 'barcode', 'price', 'stock']
            writer = csv.DictWriter(csvpr, fieldnames=fieldnames)
            writer.writerow({'product name': product_name,
                             'brand': brand,
                             'barcode': barcode,
                             'price': price,
                             'stock': stock})
            ###in main:log.info:"new product added"

    def show_invoices(self):
        """admin can see the previous invoices by this method"""
        ###get info from customer !!!write this after customer modole
        pass

    def new_admin(self):
        """add new admin to list of admins"""
        pass

    def __str__(self):
        pass
