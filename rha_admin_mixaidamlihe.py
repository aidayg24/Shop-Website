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
    zero_stock = []

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
        pas.grid(row=2, column=1, sticky=W)
        entry_password = str(pas.get()).encode()
        self.hash_entry_password = hashlib.md5(entry_password).hexdigest()

        getpass.mainloop()

    def chekpassword(self):
        if self.hash_entry_password == self.password:
            loggingadmin = StoreWindow()
            logger.info("admin log in!")
            loggingadmin.rowconfigure(0, minsize=800, weight=1)
            loggingadmin.columnconfigure(1, minsize=800, weight=1)
            taskbar_frame = Frame(loggingadmin, relief=RAISED, bd=2, bg='grey')
            btn_add = Button(taskbar_frame, text='New Product', bg='VioletRed4', command=self.add_new_product()).grid(
                row=0, column=0, sticky="ew", padx=5, pady=5)
            btn_invoice = Button(taskbar_frame, text='Invoices', bg='VioletRed4', command=self.show_invoices()).grid(
                row=1, column=0, sticky="ew", padx=5, pady=5)
            btn_change_password = Button(taskbar_frame, text='Change Password', bg='VioletRed4',
                                         command=self.change_info()).grid(row=2, column=0, sticky="ew", padx=5, pady=5)
            btn_charge = Button(taskbar_frame, text='Charge Product', bg='VioletRed4',
                                command=self.charge_stock_by_admin()).grid(row=2, column=0, sticky="ew", padx=5, pady=5)
            btn_exit = Button(taskbar_frame, text="Exit", bg='red4', command=loggingadmin.quit).grid(row=10, column=0,
                                                                                                     sticky="ew",
                                                                                                     padx=5)
            taskbar_frame.grid(row=0, column=0, sticky="ns")

            fr_main = Frame(loggingadmin, relief=RAISED, bd=1)
            file = open("product.csv", 'r')
            product_list = Listbox(fr_main, yscrollcommand=loggingadmin.scrollbar.set)
            for line in file.readlines():
                data = line.strip().split(",")
                show = "category: " + data[0] + " brand: " + data[1] + " barcode: " + data[2] + " price: " + data[
                    3] + " stock: " + data[4]
                product_list.insert(END, str(show))
            product_list.grid(row=2, column=0, sticky="ew", padx=5, pady=5)

            if self.logging_counter:
                logger.warning("First login: insecure password")
                messagebox.showwarning("Security and privacy", "Please change your password first")
                self.logging_counter = False

            if len(Admin.zero_stock) != 0:
                for product in Admin.zero_stock:
                    logger.warning("stock of " + product + " = 0")
                    messagebox.showwarning("Inventory is over!!",
                                           "The inventory of {} goods has been completed".format(product))
            loggingadmin.mainloop()
        else:
            messagebox.showerror("Failed login", "Wrong password!\nTry again")
            logger.error("login failed")
            return False

    def change_info(self):
        """the admin can change the user name and password"""
        ###we must have an item in main to change info !
        changpass = StoreWindow()
        logger.info("admin log in!")
        changpass.rowconfigure(0, minsize=800, weight=1)
        changpass.columnconfigure(1, minsize=800, weight=1)
        taskbar_frame = Frame(changpass, relief=RAISED, bd=2, bg='grey')
        btn_add = Button(taskbar_frame, text='New Product', bg='VioletRed4', command=self.add_new_product()).grid(
            row=0, column=0, sticky="ew", padx=5, pady=5)
        btn_invoice = Button(taskbar_frame, text='Invoices', bg='VioletRed4', command=self.show_invoices()).grid(
            row=1, column=0, sticky="ew", padx=5, pady=5)
        btn_change_password = Button(taskbar_frame, text='Change Password', bg='VioletRed4',
                                     command=self.change_info()).grid(row=2, column=0, sticky="ew", padx=5, pady=5)
        btn_charge = Button(taskbar_frame, text='Charge Product', bg='VioletRed4',
                            command=self.charge_stock_by_admin()).grid(row=2, column=0, sticky="ew", padx=5, pady=5)
        btn_exit = Button(taskbar_frame, text="Exit", bg='red4', command=changpass.quit).grid(row=10, column=0,
                                                                                              sticky="ew", padx=5)
        taskbar_frame.grid(row=0, column=0, sticky="ns")

        fr_main = Frame(changpass, relief=RAISED, bd=1)
        oldpas = Entry(fr_main, width=30).config(show='*')
        newpas = Entry(fr_main, width=30).config(show='*')
        log_btn = Button(fr_main, text='change', command=self.changed).grid(row=4, column=1, padx=100, pady=6)
        log_btn['state'] = 'disable'
        lbl_oldpas = ttk.Label(fr_main, text="Your old Password : ").grid(row=2, column=0)
        lbl_newpas = ttk.Label(fr_main, text="Your new Password : ").grid(row=3, column=0)
        oldpas.grid(row=2, column=1, sticky=W)
        self.newpas.grid(row=3, column=1, sticky=W)
        entry_oldpassword = str(oldpas.get()).encode()
        self.hash_entry_oldpassword = hashlib.md5(entry_oldpassword).hexdigest()
        if self.hash_entry_oldpassword == self.password:
            log_btn['state'] = 'able'

        else:
            messagebox.showerror("change Password", "Wrong password!\nTry again")
            logger.error("Unsuccessful attempt to change password")

        changpass.mainloop()

    def changed(self):
        new_pass = str(self.newpas).encode()
        hash_new_pass = hashlib.md5(new_pass).hexdigest()
        file = open("admin info.txt", "w+")
        file.write("password," + str(hash_new_pass))
        file.close()
        logger.info("Password changed")
        messagebox.showinfo("change Password", "Password changed successfully")

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

    @staticmethod
    def charge_stock_by_admin(product_name, brand):
        """ the function opens the csv file that contains the list of products
            and updates the stock(number of a product) after admin charge it."""
        file = open("product.csv", 'r')
        file_data = file.readlines()
        file.close()
        the_num = int(input("the amount of charge:\n"))
        file_overwrite = open("product.csv", 'w')
        for line in file_data:
            data = line.strip().split(",")
            if data[0] == product_name and data[1] == brand:
                stock = int(str(data[4]))
                stock += the_num
                data[4] = str(stock)
                new_data = ",".join(data)
                file_overwrite.write(new_data + "\n")
            else:
                file_overwrite.write(line)

    def __str__(self):
        pass
