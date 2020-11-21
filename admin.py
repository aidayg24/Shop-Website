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


class Admin:
    def __init__(self):
        file = open("admin info.txt", "r")
        password = file.readline().split(",")
        self.password = str(password[1])  # the password by default is 0000
        self.hash_entry_password = None

    def about(self):
        messagebox.showinfo("about maktab store",
                            "Project 4: Store Accounting\nprogramming by:\ntahere zare(raha),aida rostami,malihe mirzaii")

    def login(self):
        getpass = Toplevel()
        getpass.menubar = Menu(getpass)
        getpass.helpmenu = Menu(getpass.menubar, tearoff=0)
        getpass.helpmenu.add_command(label="About", command=self.about)
        getpass.menubar.add_cascade(label="Help", menu=getpass.helpmenu)
        getpass.config(menu=getpass.menubar)  # display the menu
        getpass.scrollbar = Scrollbar(getpass).grid(row=0, column=0, sticky="nes")
        getpass.rowconfigure(0, minsize=800, weight=1)
        getpass.columnconfigure(1, minsize=800, weight=1)
        taskbar_frame = Frame(getpass, relief=RAISED, bd=2, bg='grey')
        btn_exit = Button(taskbar_frame, text="Exit", bg='red4', command=getpass.quit).grid(row=10,
                                                                                            column=0, sticky="ew",
                                                                                            padx=5)
        ###***what is btn_exit?? you did not use this in the rest of program!
        taskbar_frame.grid(row=0, column=0, sticky="ns")

        fr_main = Frame(getpass, relief=RAISED, bd=1)
        pas = Entry(fr_main, width=30)
        pas.config(show='*')
        lbl_pas = ttk.Label(fr_main, text="Your Password : ").grid(row=2, column=0)
        pas.grid(row=2, column=1, sticky=W)

        entry_password = pas.get().lower().strip().encode()
        self.hash_entry_password = hashlib.md5(entry_password).hexdigest()
        log_btn = Button(fr_main, text='Login', command=self.chekpassword).grid(row=3, column=1,padx=100, pady=6)
        fr_main.grid(row=0, column=1, sticky="nsew")
        getpass.mainloop()

    def chekpassword(self):
        entrypass = self.hash_entry_password
        if entrypass == self.password:
            loggingadmin = Toplevel()
            loggingadmin.menubar = Menu(loggingadmin)
            loggingadmin.helpmenu = Menu(loggingadmin.menubar, tearoff=0)
            loggingadmin.helpmenu.add_command(label="About", command=self.about)
            loggingadmin.menubar.add_cascade(label="Help", menu=loggingadmin.helpmenu)
            loggingadmin.config(menu=loggingadmin.menubar)  # display the menu
            loggingadmin.scrollbar = Scrollbar(loggingadmin).grid(row=0, column=0, sticky="nes")
            logger.info("admin log in!")
            loggingadmin.rowconfigure(0, minsize=800, weight=1)
            loggingadmin.columnconfigure(1, minsize=800, weight=1)
            taskbar_frame = Frame(loggingadmin, relief=RAISED, bd=2, bg='grey')
            btn_add = Button(taskbar_frame, text='New Product', bg='VioletRed4', command=self.add_new_product).grid(
                row=0, column=0, sticky="ew", padx=5, pady=5)
            btn_invoice = Button(taskbar_frame, text='Invoices', bg='VioletRed4', command=self.show_invoices).grid(
                row=1, column=0, sticky="ew", padx=5, pady=5)
            btn_charge = Button(taskbar_frame, text='Charge Product', bg='VioletRed4',
                                command=self.charge_stock_by_admin).grid(row=3, column=0, sticky="ew", padx=5, pady=5)
            btn_storeroom = Button(taskbar_frame, text='storeroom', bg='VioletRed4',
                                   command=self.seeproduct).grid(row=4, column=0, sticky="ew", padx=5,pady=5)
            btn_exit = Button(taskbar_frame, text="Exit", bg='red4', command=loggingadmin.quit).grid(row=10, column=0,
                                                                                                     sticky="ew",
                                                                                                     padx=5)
            taskbar_frame.grid(row=0, column=0, sticky="ns")

            fr_main = Frame(loggingadmin, relief=RAISED, bd=1)
            fr_main.grid(row=0, column=1, sticky="nsew")

            file = open("product.csv", 'r')
            line_counter=0
            for line in file.readlines():
                data = line.strip().split(",")
                if line_counter>0:
                    if int(data[4])==0:
                        messagebox.showerror('storeroom','Inventory with {} barcode is exhausted'.format(data[2]))
                        logger.warning('Inventory with {} barcode is exhausted'.format(data[2]))
                line_counter+=1

            loggingadmin.mainloop()
        else:
            messagebox.showerror("Failed login", "Wrong password!\nTry again")
            logger.error("login failed")
            return False

    def add_new_product(self):
        """admin can add new product to the list of products and updates the entrepot"""

        addproduct = Toplevel()
        addproduct.menubar = Menu(addproduct)
        addproduct.helpmenu = Menu(addproduct.menubar, tearoff=0)
        addproduct.helpmenu.add_command(label="About", command=self.about)
        addproduct.menubar.add_cascade(label="Help", menu=addproduct.helpmenu)
        addproduct.config(menu=addproduct.menubar)  # display the menu
        addproduct.scrollbar = Scrollbar(addproduct).grid(row=0, column=0, sticky="nes")

        addproduct.rowconfigure(0, minsize=800, weight=1)
        addproduct.columnconfigure(1, minsize=800, weight=1)
        taskbar_frame = Frame(addproduct, relief=RAISED, bd=2, bg='grey')
        btn_add = Button(taskbar_frame, text='New Product', bg='VioletRed4', command=self.add_new_product).grid(
            row=0, column=0, sticky="ew", padx=5, pady=5)
        btn_invoice = Button(taskbar_frame, text='Invoices', bg='VioletRed4', command=self.show_invoices).grid(
            row=1, column=0, sticky="ew", padx=5, pady=5)
        btn_charge = Button(taskbar_frame, text='Charge Product', bg='VioletRed4',
                            command=self.charge_stock_by_admin).grid(row=3, column=0, sticky="ew", padx=5, pady=5)
        btn_storeroom = Button(taskbar_frame, text='storeroom', bg='VioletRed4',
                               command=self.seeproduct).grid(row=4, column=0, sticky="ew", padx=5, pady=5)
        btn_exit = Button(taskbar_frame, text="Exit", bg='red4', command=addproduct.quit).grid(row=10, column=0,
                                                                                               sticky="ew", padx=5)
        taskbar_frame.grid(row=0, column=0, sticky="ns")

        fr_main = Frame(addproduct, relief=RAISED, bd=1)
        self.product_name = Entry(fr_main, width=30)
        self.brand = Entry(fr_main, width=30)
        self.barcode = Entry(fr_main, width=30)
        self.price = Entry(fr_main, width=30)
        self.stock = Entry(fr_main, width=30)
        add_btn = Button(fr_main, text='Add', command=self.adding).grid(row=7, column=1, padx=100, pady=6)
        lbl_product_name = ttk.Label(fr_main, text="product name : ").grid(row=2, column=0)
        lbl_brand = ttk.Label(fr_main, text="brand : ").grid(row=3, column=0)
        lbl_barcode = ttk.Label(fr_main, text="barcode : ").grid(row=4, column=0)
        lbl_price = ttk.Label(fr_main, text="price : ").grid(row=5, column=0)
        lbl_stock = ttk.Label(fr_main, text="stock : ").grid(row=6, column=0)
        self.product_name.grid(row=2, column=1, sticky=W)
        self.brand.grid(row=3, column=1, sticky=W)
        self.barcode.grid(row=4, column=1, sticky=W)
        self.price.grid(row=5, column=1, sticky=W)
        self.stock.grid(row=6, column=1, sticky=W)
        fr_main.grid(row=0, column=1, sticky="nsew")

        addproduct.mainloop()

    def adding(self):
        productname = self.product_name.get().lower().strip()
        brand = self.brand.get().lower().strip()
        barcode = self.barcode.get().lower().strip()
        price = self.price.get().lower().strip()
        stock = self.stock.get().lower().strip()

        with open('product.csv', 'a', newline='') as csvpr:
            fieldnames = ['product name', 'brand', 'barcode', 'price', 'stock']
            writer = csv.DictWriter(csvpr, fieldnames=fieldnames)
            writer.writerow({'product name': productname,
                             'brand': brand,
                             'barcode': barcode,
                             'price': price,
                             'stock': stock})
            logger.info("new product added")
            messagebox.showinfo('Add product', 'new product added')

    def show_invoices(self):
        seeinvokes = Toplevel()
        seeinvokes.menubar = Menu(seeinvokes)
        seeinvokes.helpmenu = Menu(seeinvokes.menubar, tearoff=0)
        seeinvokes.helpmenu.add_command(label="About", command=self.about)
        seeinvokes.menubar.add_cascade(label="Help", menu=seeinvokes.helpmenu)
        seeinvokes.config(menu=seeinvokes.menubar)  # display the menu
        seeinvokes.scrollbar = Scrollbar(seeinvokes).grid(row=0, column=0, sticky="nes")

        seeinvokes.rowconfigure(0, minsize=800, weight=1)
        seeinvokes.columnconfigure(1, minsize=800, weight=1)
        taskbar_frame = Frame(seeinvokes, relief=RAISED, bd=2, bg='grey')
        btn_add = Button(taskbar_frame, text='New Product', bg='VioletRed4', command=self.add_new_product).grid(
            row=0, column=0, sticky="ew", padx=5, pady=5)
        btn_invoice = Button(taskbar_frame, text='Invoices', bg='VioletRed4', command=self.show_invoices).grid(
            row=1, column=0, sticky="ew", padx=5, pady=5)
        btn_charge = Button(taskbar_frame, text='Charge Product', bg='VioletRed4',
                            command=self.charge_stock_by_admin).grid(row=3, column=0, sticky="ew", padx=5, pady=5)
        btn_storeroom = Button(taskbar_frame, text='storeroom', bg='VioletRed4',
                               command=self.seeproduct).grid(row=4, column=0, sticky="ew", padx=5, pady=5)
        btn_exit = Button(taskbar_frame, text="Exit", bg='red4', command=seeinvokes.quit).grid(row=10, column=0,
                                                                                               sticky="ew", padx=5)
        taskbar_frame.grid(row=0, column=0, sticky="ns")

        fr_main = Frame(seeinvokes, relief=RAISED, bd=1)
        file = open("invoice.csv", "r")
        row=1
        for line in file.readlines():
            data = line.strip().split(",")
            productname = Label(fr_main, text=data[0].strip()+' , '+data[1].strip())
            barcode = Label(fr_main, text=data[2].strip())
            number = Label(fr_main, text=data[3].strip())
            price = Label(fr_main, text=data[4].strip())
            sum = Label(fr_main, text=data[5].strip())
            totallsum = Label(fr_main, text=data[6].strip())
            productname.grid(row=row, column=0, sticky="w", padx=5, pady=5)
            barcode.grid(row=row, column=1, sticky="w", padx=5, pady=5)
            number.grid(row=row, column=2, sticky="w", padx=5, pady=5)
            price.grid(row=row, column=3, sticky="w", padx=5, pady=5)
            sum.grid(row=row, column=4, sticky="w", padx=5, pady=5)
            totallsum.grid(row=row, column=5, sticky="w", padx=5, pady=5)

            row+=1

        fr_main.grid(row=0, column=1, sticky="nsew")
        seeinvokes.mainloop()

    def seeproduct(self):
        loggingadmin = Toplevel()
        loggingadmin.menubar = Menu(loggingadmin)
        loggingadmin.helpmenu = Menu(loggingadmin.menubar, tearoff=0)
        loggingadmin.helpmenu.add_command(label="About", command=self.about)
        loggingadmin.menubar.add_cascade(label="Help", menu=loggingadmin.helpmenu)
        loggingadmin.config(menu=loggingadmin.menubar)  # display the menu
        loggingadmin.scrollbar = Scrollbar(loggingadmin).grid(row=0, column=0, sticky="nes")
        logger.info("admin log in!")
        loggingadmin.rowconfigure(0, minsize=800, weight=1)
        loggingadmin.columnconfigure(1, minsize=800, weight=1)
        taskbar_frame = Frame(loggingadmin, relief=RAISED, bd=2, bg='grey')
        btn_add = Button(taskbar_frame, text='New Product', bg='VioletRed4', command=self.add_new_product).grid(
            row=0, column=0, sticky="ew", padx=5, pady=5)
        btn_invoice = Button(taskbar_frame, text='Invoices', bg='VioletRed4', command=self.show_invoices).grid(
            row=1, column=0, sticky="ew", padx=5, pady=5)
        btn_charge = Button(taskbar_frame, text='Charge Product', bg='VioletRed4',
                            command=self.charge_stock_by_admin).grid(row=3, column=0, sticky="ew", padx=5, pady=5)
        btn_storeroom = Button(taskbar_frame, text='storeroom', bg='VioletRed4',
                               command=self.seeproduct).grid(row=4, column=0, sticky="ew", padx=5, pady=5)
        btn_exit = Button(taskbar_frame, text="Exit", bg='red4', command=loggingadmin.quit).grid(row=10, column=0,
                                                                                                 sticky="ew",
                                                                                                 padx=5)
        taskbar_frame.grid(row=0, column=0, sticky="ns")

        fr_main = Frame(loggingadmin, relief=RAISED, bd=1)
        file = open("product.csv", 'r')
        row=0
        for line in file.readlines():
            data = line.strip().split(",")
            category = Label(fr_main, text=data[0])
            brand = Label(fr_main, text=data[1])
            barcode = Label(fr_main, text=data[2])
            price = Label(fr_main, text=data[3])
            stock = Label(fr_main, text=data[4])
            category.grid(row=row, column=0, sticky="w", padx=5, pady=5)
            brand.grid(row=row, column=1, sticky="w", padx=5, pady=5)
            barcode.grid(row=row, column=2, sticky="w", padx=5, pady=5)
            price.grid(row=row, column=3, sticky="w", padx=5, pady=5)
            stock.grid(row=row, column=4, sticky="w", padx=5, pady=5)
            row += 1
        fr_main.grid(row=0, column=1, sticky="nsew")
        file = open("product.csv", 'r')
    def charge_stock_by_admin(self):
        charge = Toplevel()
        charge.menubar = Menu(charge)
        charge.helpmenu = Menu(charge.menubar, tearoff=0)
        charge.helpmenu.add_command(label="About", command=self.about)
        charge.menubar.add_cascade(label="Help", menu=charge.helpmenu)
        charge.config(menu=charge.menubar)  # display the menu
        charge.scrollbar = Scrollbar(charge).grid(row=0, column=0, sticky="nes")
        logger.info("admin log in!")
        charge.rowconfigure(0, minsize=800, weight=1)
        charge.columnconfigure(1, minsize=800, weight=1)
        taskbar_frame = Frame(charge, relief=RAISED, bd=2, bg='grey')
        btn_add = Button(taskbar_frame, text='New Product', bg='VioletRed4', command=self.add_new_product).grid(
            row=0, column=0, sticky="ew", padx=5, pady=5)
        btn_invoice = Button(taskbar_frame, text='Invoices', bg='VioletRed4', command=self.show_invoices).grid(
            row=1, column=0, sticky="ew", padx=5, pady=5)
        btn_charge = Button(taskbar_frame, text='Charge Product', bg='VioletRed4',
                            command=self.charge_stock_by_admin).grid(row=3, column=0, sticky="ew", padx=5, pady=5)
        btn_storeroom = Button(taskbar_frame, text='storeroom', bg='VioletRed4',
                               command=self.seeproduct).grid(row=4, column=0, sticky="ew", padx=5, pady=5)
        btn_exit = Button(taskbar_frame, text="Exit", bg='red4', command=charge.quit).grid(row=10, column=0,
                                                                                           sticky="ew", padx=5)
        taskbar_frame.grid(row=0, column=0, sticky="ns")

        fr_main = Frame(charge, relief=RAISED, bd=1)
        self.barcode = Entry(fr_main, width=30)
        self.num = Scale(fr_main, from_=0, to=100, orient=HORIZONTAL)
        charge_btn = Button(fr_main, text='Charge', command=self.charged).grid(row=4, column=1, padx=100, pady=6)
        lbl_barcode = ttk.Label(fr_main, text="barcode : ").grid(row=2, column=0)
        lbl_num = ttk.Label(fr_main, text="How many? ").grid(row=3, column=0)
        self.barcode.grid(row=2, column=1, sticky=W)
        self.num.grid(row=3, column=1, sticky=W)
        fr_main.grid(row=0, column=1, sticky="nsew")

    def charged(self):
        """ the function opens the csv file that contains the list of products
            and updates the stock(number of a product) after admin charge it."""
        file = open("product.csv", 'r')
        file_data = file.readlines()
        file.close()
        file_overwrite = open("product.csv", 'w')
        for line in file_data:
            data = line.strip().split(",")
            if data[2].strip() == self.barcode.get().lower().strip():
                stock = int(str(data[4]))
                print(int(self.num.get()))
                stock += int(self.num.get())
                data[4] = str(stock)
                new_data = ",".join(data)
                file_overwrite.write(new_data + "\n")
            else:
                new_data = ",".join(data)
                file_overwrite.write(new_data + "\n")
        file_overwrite.close()
        messagebox.showinfo('charge product', 'inventory increased')
        logger.info('The inventory was charged')
