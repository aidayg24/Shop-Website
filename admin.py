import csv# importing csv
from tkinter import ttk# importing ttk module
from tkinter import *# importing tkinter library
from tkinter import messagebox# importing messagebox module
import hashlib#importing hashlib module
import logging  # importing tkinter library for log information

# Define the data logging format:
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename="logfile.log",
                    level=logging.DEBUG,
                    format=LOG_FORMAT,
                    filemode='a')
logger = logging.getLogger()


class Admin:# Define the admin class to organize the admin's tasks and authority
    def __init__(self):
        file = open("admin info.txt", "r")
        password = file.readline().split(",")
        self.password = str(password[1])  # the password by default is 0000
        self.hash_entry_password = None

    def about(self):# This function displays information about the application
        messagebox.showinfo("about maktab store",
                            "Project 4: Store Accounting\nprogramming by:\ntahere zare(raha),aida rostami,malihe mirzaii")

    def login(self):
    #A window will open so that the admin can enter her password
        getpass = Toplevel()# making a top window

        getpass.menubar = Menu(getpass)
        getpass.helpmenu = Menu(getpass.menubar, tearoff=0)
        getpass.helpmenu.add_command(label="About", command=self.about)
        getpass.menubar.add_cascade(label="Help", menu=getpass.helpmenu)
        getpass.config(menu=getpass.menubar)  # display the menu

        # Configure window rows and column:
        getpass.rowconfigure(0, minsize=800, weight=1)
        getpass.columnconfigure(1, minsize=800, weight=1)

        # Definition of taskbar:
        taskbar_frame = Frame(getpass, relief=RAISED, bd=2, bg='grey')
        btn_exit = Button(taskbar_frame, text="Exit", bg='red4', command=getpass.quit).grid(row=10,column=0, sticky="ew",padx=5)
        taskbar_frame.grid(row=0, column=0, sticky="ns")

        # Define the main frame:
        fr_main = Frame(getpass, relief=RAISED, bd=1)
        # get password:
        pas = Entry(fr_main, width=30)
        #An asterisk is displayed when entering a password for security issues
        pas.config(show='*')
        lbl_pas = ttk.Label(fr_main, text="Your Password : ").grid(row=2, column=0)
        pas.grid(row=2, column=1, sticky=W)

        entry_password = pas.get().lower().strip().encode()
        self.hash_entry_password = hashlib.md5(entry_password).hexdigest()
        log_btn = Button(fr_main, text='Login', command=self.chekpassword).grid(row=3, column=1,padx=100, pady=6)
        fr_main.grid(row=0, column=1, sticky="nsew")

        getpass.mainloop() # creating a loop for the main window to store the changes

    def chekpassword(self):
        entrypass = self.hash_entry_password
        if entrypass == self.password: #If the password entered is correct, the login window will open
            logger.info("admin log in!")

            loggingadmin = Toplevel() # making a top window

            loggingadmin.menubar = Menu(loggingadmin)
            loggingadmin.helpmenu = Menu(loggingadmin.menubar, tearoff=0)
            loggingadmin.helpmenu.add_command(label="About", command=self.about)
            loggingadmin.menubar.add_cascade(label="Help", menu=loggingadmin.helpmenu)
            loggingadmin.config(menu=loggingadmin.menubar)  # display the menu

            # Configure window rows and column:
            loggingadmin.rowconfigure(0, minsize=800, weight=1)
            loggingadmin.columnconfigure(1, minsize=800, weight=1)

            # Definition of taskbar:
            taskbar_frame = Frame(loggingadmin, relief=RAISED, bd=2, bg='grey')
            btn_add = Button(taskbar_frame, text='New Product', bg='VioletRed4', command=self.add_new_product).grid(row=0, column=0, sticky="ew", padx=5, pady=5)
            btn_invoice = Button(taskbar_frame, text='Invoices', bg='VioletRed4', command=self.show_invoices).grid(row=1, column=0, sticky="ew", padx=5, pady=5)
            btn_charge = Button(taskbar_frame, text='Charge Product', bg='VioletRed4',command=self.charge_stock_by_admin).grid(row=3, column=0, sticky="ew", padx=5, pady=5)
            btn_storeroom = Button(taskbar_frame, text='storeroom', bg='VioletRed4',command=self.seeproduct).grid(row=4, column=0, sticky="ew", padx=5,pady=5)
            btn_exit = Button(taskbar_frame, text="Exit", bg='red4', command=loggingadmin.quit).grid(row=10, column=0,sticky="ew",padx=5)
            taskbar_frame.grid(row=0, column=0, sticky="ns")

            #Warns the admin if the stock is out of stock:
            file = open("product.csv", 'r')
            line_counter=0
            for line in file.readlines():
                data = line.strip().split(",")
                if line_counter>0:
                    if int(data[4])==0:
                        messagebox.showerror('storeroom','Inventory with {} barcode is exhausted'.format(data[2]))
                        logger.warning('Inventory with {} barcode is exhausted'.format(data[2]))
                line_counter+=1

            loggingadmin.mainloop() # creating a loop for the main window to store the changes
        else:
            #If the password is not correct, it gives an error:
            messagebox.showerror("Failed login", "Wrong password!\nTry again")
            logger.error("login failed")

    def add_new_product(self):
        """admin can add new product to the list of products and updates the entrepot"""

        addproduct = Toplevel() # making a top window

        addproduct.menubar = Menu(addproduct)
        addproduct.helpmenu = Menu(addproduct.menubar, tearoff=0)
        addproduct.helpmenu.add_command(label="About", command=self.about)
        addproduct.menubar.add_cascade(label="Help", menu=addproduct.helpmenu)
        addproduct.config(menu=addproduct.menubar)  # display the menu

        # Configure window rows and column:
        addproduct.rowconfigure(0, minsize=800, weight=1)
        addproduct.columnconfigure(1, minsize=800, weight=1)

        # Definition of taskbar:
        taskbar_frame = Frame(addproduct, relief=RAISED, bd=2, bg='grey')
        btn_add = Button(taskbar_frame, text='New Product', bg='VioletRed4', command=self.add_new_product).grid(row=0, column=0, sticky="ew", padx=5, pady=5)
        btn_invoice = Button(taskbar_frame, text='Invoices', bg='VioletRed4', command=self.show_invoices).grid(row=1, column=0, sticky="ew", padx=5, pady=5)
        btn_charge = Button(taskbar_frame, text='Charge Product', bg='VioletRed4',command=self.charge_stock_by_admin).grid(row=3, column=0, sticky="ew", padx=5, pady=5)
        btn_storeroom = Button(taskbar_frame, text='storeroom', bg='VioletRed4',command=self.seeproduct).grid(row=4, column=0, sticky="ew", padx=5, pady=5)
        btn_exit = Button(taskbar_frame, text="Exit", bg='red4', command=addproduct.quit).grid(row=10, column=0,sticky="ew", padx=5)
        taskbar_frame.grid(row=0, column=0, sticky="ns")

        # Define the main frame:
        fr_main = Frame(addproduct, relief=RAISED, bd=1)
        #Receives product information for registration from the admin
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

        addproduct.mainloop() # creating a loop for the main window to store the changes

    def adding(self):
        #In order to have less problems in the future, we will use .lower().strip()
        productname = self.product_name.get().lower().strip()
        brand = self.brand.get().lower().strip()
        barcode = self.barcode.get().lower().strip()
        price = self.price.get().lower().strip()
        stock = self.stock.get().lower().strip()

        #We save the entered information in the warehouse Excel file
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
        #A new window will open to display all registered invoices
        seeinvokes = Toplevel() # making a top window

        seeinvokes.menubar = Menu(seeinvokes)
        seeinvokes.helpmenu = Menu(seeinvokes.menubar, tearoff=0)
        seeinvokes.helpmenu.add_command(label="About", command=self.about)
        seeinvokes.menubar.add_cascade(label="Help", menu=seeinvokes.helpmenu)
        seeinvokes.config(menu=seeinvokes.menubar)  # display the menu

        # Configure window rows and column:
        seeinvokes.rowconfigure(0, minsize=800, weight=1)
        seeinvokes.columnconfigure(1, minsize=800, weight=1)

        # Definition of taskbar:
        taskbar_frame = Frame(seeinvokes, relief=RAISED, bd=2, bg='grey')
        btn_add = Button(taskbar_frame, text='New Product', bg='VioletRed4', command=self.add_new_product).grid(row=0, column=0, sticky="ew", padx=5, pady=5)
        btn_invoice = Button(taskbar_frame, text='Invoices', bg='VioletRed4', command=self.show_invoices).grid(row=1, column=0, sticky="ew", padx=5, pady=5)
        btn_charge = Button(taskbar_frame, text='Charge Product', bg='VioletRed4',command=self.charge_stock_by_admin).grid(row=3, column=0, sticky="ew", padx=5, pady=5)
        btn_storeroom = Button(taskbar_frame, text='storeroom', bg='VioletRed4',command=self.seeproduct).grid(row=4, column=0, sticky="ew", padx=5, pady=5)
        btn_exit = Button(taskbar_frame, text="Exit", bg='red4', command=seeinvokes.quit).grid(row=10, column=0,sticky="ew", padx=5)
        taskbar_frame.grid(row=0, column=0, sticky="ns")

        # Define the main frame:
        fr_main = Frame(seeinvokes, relief=RAISED, bd=1)
        # The invoices table is shown to her
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
        seeinvokes.mainloop() # creating a loop for the main window to store the changes

    def seeproduct(self):
        #A window will open so that the admin can see a view of the warehouse
        loggingadmin = Toplevel()# making a top window

        loggingadmin.menubar = Menu(loggingadmin)
        loggingadmin.helpmenu = Menu(loggingadmin.menubar, tearoff=0)
        loggingadmin.helpmenu.add_command(label="About", command=self.about)
        loggingadmin.menubar.add_cascade(label="Help", menu=loggingadmin.helpmenu)
        loggingadmin.config(menu=loggingadmin.menubar)  # display the menu

        # Configure window rows and column:
        loggingadmin.rowconfigure(0, minsize=800, weight=1)
        loggingadmin.columnconfigure(1, minsize=800, weight=1)

        # Definition of taskbar:
        taskbar_frame = Frame(loggingadmin, relief=RAISED, bd=2, bg='grey')
        btn_add = Button(taskbar_frame, text='New Product', bg='VioletRed4', command=self.add_new_product).grid(row=0, column=0, sticky="ew", padx=5, pady=5)
        btn_invoice = Button(taskbar_frame, text='Invoices', bg='VioletRed4', command=self.show_invoices).grid(row=1, column=0, sticky="ew", padx=5, pady=5)
        btn_charge = Button(taskbar_frame, text='Charge Product', bg='VioletRed4',command=self.charge_stock_by_admin).grid(row=3, column=0, sticky="ew", padx=5, pady=5)
        btn_storeroom = Button(taskbar_frame, text='storeroom', bg='VioletRed4',command=self.seeproduct).grid(row=4, column=0, sticky="ew", padx=5, pady=5)
        btn_exit = Button(taskbar_frame, text="Exit", bg='red4', command=loggingadmin.quit).grid(row=10, column=0,sticky="ew",padx=5)
        taskbar_frame.grid(row=0, column=0, sticky="ns")

        # Define the main frame:
        fr_main = Frame(loggingadmin, relief=RAISED, bd=1)
        #Reads and displays inventory information from the file
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
        file.close()

        fr_main.grid(row=0, column=1, sticky="nsew")

        loggingadmin.mainloop() # creating a loop for the main window to store the changes

    def charge_stock_by_admin(self):
        #A window will open so that the admin can increase the inventory of the desired product by entering the information
        charge = Toplevel()# making a top window

        charge.menubar = Menu(charge)
        charge.helpmenu = Menu(charge.menubar, tearoff=0)
        charge.helpmenu.add_command(label="About", command=self.about)
        charge.menubar.add_cascade(label="Help", menu=charge.helpmenu)
        charge.config(menu=charge.menubar)  # display the menu

        # Configure window rows and column:
        charge.rowconfigure(0, minsize=800, weight=1)
        charge.columnconfigure(1, minsize=800, weight=1)

        # Definition of taskbar:
        taskbar_frame = Frame(charge, relief=RAISED, bd=2, bg='grey')
        btn_add = Button(taskbar_frame, text='New Product', bg='VioletRed4', command=self.add_new_product).grid(row=0, column=0, sticky="ew", padx=5, pady=5)
        btn_invoice = Button(taskbar_frame, text='Invoices', bg='VioletRed4', command=self.show_invoices).grid(row=1, column=0, sticky="ew", padx=5, pady=5)
        btn_charge = Button(taskbar_frame, text='Charge Product', bg='VioletRed4',command=self.charge_stock_by_admin).grid(row=3, column=0, sticky="ew", padx=5, pady=5)
        btn_storeroom = Button(taskbar_frame, text='storeroom', bg='VioletRed4',command=self.seeproduct).grid(row=4, column=0, sticky="ew", padx=5, pady=5)
        btn_exit = Button(taskbar_frame, text="Exit", bg='red4', command=charge.quit).grid(row=10, column=0,sticky="ew", padx=5)
        taskbar_frame.grid(row=0, column=0, sticky="ns")

        # Define the main frame:
        fr_main = Frame(charge, relief=RAISED, bd=1)
        self.barcode = Entry(fr_main, width=30)
        #The admin determines the desired charge amount in the allowable range by dragging the scale:
        self.num = Scale(fr_main, from_=0, to=100, orient=HORIZONTAL)
        charge_btn = Button(fr_main, text='Charge', command=self.charged).grid(row=4, column=1, padx=100, pady=6)
        lbl_barcode = ttk.Label(fr_main, text="barcode : ").grid(row=2, column=0)
        lbl_num = ttk.Label(fr_main, text="How many? ").grid(row=3, column=0)
        self.barcode.grid(row=2, column=1, sticky=W)
        self.num.grid(row=3, column=1, sticky=W)

        fr_main.grid(row=0, column=1, sticky="nsew")

        charge.mainloop() # creating a loop for the main window to store the changes

    def charged(self):
        """ the function opens the csv file that contains the list of products
            and updates the stock(number of a product) after admin charge it."""
        file = open("product.csv", 'r')
        file_data = file.readlines()
        file.close()
        file_overwrite = open("product.csv", 'w')
        line_counter=1
        for line in file_data:
            if line_counter>1:
                data = line.strip().split(",")
                if data[2].strip() == self.barcode.get().lower().strip():
                    stock = int(str(data[4]))
                    stock += int(self.num.get())
                    data[4] = str(stock)
                    new_data = ",".join(data)
                    file_overwrite.write(new_data + "\n")
                else:
                    new_data = ",".join(data)
                    file_overwrite.write(new_data + "\n")
            else:
                file_overwrite.write(line)
        file_overwrite.close()
        messagebox.showinfo('charge product', 'inventory increased')
        logger.info('The inventory was charged')
