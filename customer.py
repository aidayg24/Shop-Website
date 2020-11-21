import csv  # importing csv
from tkinter import ttk  # importing ttk module
from tkinter import *  # importing tkinter library
from tkinter import messagebox  # importing messagebox module
import logging  # importing tkinter library for log information
from admin import Admin  # import class Admin from admin module

admin = Admin()  # make an object from class admin

# Define the data logging format:
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename="logfile.log",
                    level=logging.DEBUG,
                    format=LOG_FORMAT,
                    filemode='a')
logger = logging.getLogger()


class Customer:  # Define the customer class to organize the client's tasks and authority
    def __init__(self):
        # for save information use tuple cuse tuple is a collection which is ordered and unchangeable.
        self.basket = {'info': ('name', 'brand', 'barcode', 'number', 'price for one', 'hole price', 'total sum')}

    def about(self):  # This function displays information about the application
        messagebox.showinfo("about maktab store",
                            "Project 4: Store Accounting\nprogramming by:\ntahere zare(raha),aida rostami,malihe mirzaii")

    def add_to_basket(self):
        # A window will open for the customer to enter the product and brand name and the number she wants to make a purchase
        addtobaskt = Toplevel()  # making a top window

        addtobaskt.menubar = Menu(addtobaskt)
        addtobaskt.helpmenu = Menu(addtobaskt.menubar, tearoff=0)
        addtobaskt.helpmenu.add_command(label="About", command=self.about)
        addtobaskt.menubar.add_cascade(label="Help", menu=addtobaskt.helpmenu)
        addtobaskt.config(menu=addtobaskt.menubar)  # display the menu

        # Configure window rows and column
        addtobaskt.rowconfigure(0, minsize=800, weight=1)
        addtobaskt.columnconfigure(1, minsize=800, weight=1)

        # Definition of taskbar:
        taskbar_frame = Frame(addtobaskt, relief=RAISED, bd=2, bg='grey')
        btn_admin = Button(taskbar_frame, text='Admin', bg='firebrick4', command=admin.login).grid(row=0, column=0,
                                                                                                   sticky="ew", padx=5,
                                                                                                   pady=5)
        btn_bsktet = Button(taskbar_frame, text='basket', bg='VioletRed4', command=self.showbasket).grid(row=2,
                                                                                                         column=0,
                                                                                                         sticky="ew",
                                                                                                         padx=5, pady=5)
        btn_exit = Button(taskbar_frame, text="Exit", bg='red4', command=addtobaskt.quit).grid(row=10, column=0,
                                                                                               sticky="ew", padx=5)
        taskbar_frame.grid(row=0, column=0, sticky="ns")

        # Define the main frame:
        fr_main = Frame(addtobaskt, relief=RAISED, bd=1)
        # To buy name, brand, number is entered:
        self.product_name = Entry(fr_main, width=30)  # Entry == input
        self.brand = Entry(fr_main, width=30)
        self.number = Spinbox(fr_main, from_=0, to=100)  # give a number in range(0,100)
        add_btn = Button(fr_main, text='Add to basket', command=self.added).grid(row=7, column=1, padx=100, pady=6)
        lbl_product_name = ttk.Label(fr_main, text="product name : ").grid(row=2, column=0)
        lbl_brand = ttk.Label(fr_main, text="brand : ").grid(row=3, column=0)
        self.product_name.grid(row=2, column=1, sticky=W)
        self.brand.grid(row=3, column=1, sticky=W)
        self.number.grid(row=4, column=1, sticky=W)
        fr_main.grid(row=0, column=1, sticky="nsew")

        addtobaskt.mainloop()  # creating a loop for the main window to store the changes

    def added(self):
        self.price = 0  # Total purchase total
        barcode = None  # Defined for when the barcode was not found

        # Using the name and brand, we find the barcode of the product:
        file = open("product.csv", 'r')
        for line in file.readlines():
            data = line.strip().split(",")
            if self.product_name.get().lower().strip() == data[0] and self.brand.get().lower().strip() == data[1]:
                barcode = data[2]
                if int(self.number.get().strip()) <= int(data[4]):  # Check inventory number
                    the_price_of_one = int(data[3])
                    # We store the product information with the barcode found in the basket
                    self.basket[barcode] = (data[0], data[1], data[2], int(self.number.get().strip()), data[3],
                                            the_price_of_one * int(self.number.get().strip()), None)
                    self.price += the_price_of_one * int(self.number.get().strip())
                    messagebox.showinfo('Buy', 'Product added to your basket')
                    logger.info('An item was added to a customers basket')
                else:
                    messagebox.showerror('Buy', 'The amount you want is more than the inventory')
                    logger.error('Unsuccessful attempt to buy goods : Insufficient inventory')

    def showbasket(self):
        # A window will open to display the customer invoice as a table and finalize it if desired
        baskett = Toplevel()  # making a top window

        baskett.menubar = Menu(baskett)
        baskett.helpmenu = Menu(baskett.menubar, tearoff=0)
        baskett.helpmenu.add_command(label="About", command=self.about)
        baskett.menubar.add_cascade(label="Help", menu=baskett.helpmenu)
        baskett.config(menu=baskett.menubar)  # display the menu

        # Configure window rows and column
        baskett.rowconfigure(0, minsize=800, weight=1)
        baskett.columnconfigure(1, minsize=800, weight=1)

        # Definition of taskbar:
        taskbar_frame = Frame(baskett, relief=RAISED, bd=2, bg='grey')
        btn_admin = Button(taskbar_frame, text='Admin', bg='firebrick4', command=admin.login).grid(row=0, column=0,
                                                                                                   sticky="ew", padx=5,
                                                                                                   pady=5)
        btn_cart = Button(taskbar_frame, text='basket', bg='VioletRed4', command=self.showbasket).grid(row=2, column=0,
                                                                                                       sticky="ew",
                                                                                                       padx=5, pady=5)
        btn_exit = Button(taskbar_frame, text="Exit", bg='red4', command=baskett.quit).grid(row=10, column=0,
                                                                                            sticky="ew", padx=5)
        taskbar_frame.grid(row=0, column=0, sticky="ns")

        # Define the main frame:
        fr_main = Frame(baskett, relief=RAISED, bd=1)

        # The customer invoice table is shown to her
        # Table top:
        producnamebrand = Label(fr_main, text='info', bg='tomato4')
        price = Label(fr_main, text='price of one', bg='tomato4')
        number = Label(fr_main, text='counter', bg='tomato4')
        sum = Label(fr_main, text='sum', bg='tomato4')
        producnamebrand.grid(row=0, column=0, sticky="w", padx=5, pady=5)
        number.grid(row=0, column=1, sticky="w", padx=5, pady=5)
        price.grid(row=0, column=2, sticky="w", padx=5, pady=5)
        sum.grid(row=0, column=3, sticky="w", padx=5, pady=5)

        # Table information:
        row = 2
        self.totallsum = 0
        for product in self.basket.values():
            if row > 2:
                producnamebrand = Label(fr_main, text=product[0] + ',' + product[1])
                price = Label(fr_main, text=product[4])
                number = Label(fr_main, text=product[3])

                self.totallsum += int(product[5])
                sum = Label(fr_main, text=str(product[5]))
                producnamebrand.grid(row=row, column=0, sticky="w", padx=5, pady=5)
                number.grid(row=row, column=1, sticky="w", padx=5, pady=5)
                price.grid(row=row, column=2, sticky="w", padx=5, pady=5)
                sum.grid(row=row, column=3, sticky="w", padx=5, pady=5)
            row += 1

        # The final addition to the shopping cart:
        totall = Label(fr_main, text='totall sum = ' + str(self.totallsum))
        totall.grid(row=row, column=3, sticky="w", padx=5, pady=5)

        # Purchase registration:
        buy_btn = Button(fr_main, text="Click if you want your purchase to be final", bg='red4', command=self.buy)
        buy_btn.grid(row=row + 1, sticky="w", padx=5, pady=5)

        fr_main.grid(row=0, column=1, sticky="nsew")

        baskett.mainloop()  # creating a loop for the main window to store the changes

    def buy(self):
        # This function records the customer's purchase:
        messagebox.showinfo('Buy', 'Your purchase has been registered')
        logger.info('A purchase was made')

        # Records the purchase information in the invoice file
        with open('invoice.csv', 'a', newline='') as invoice:
            fieldnames = ['category', 'brand', 'barcode', 'number', 'price of one product', 'hole price', 'totall sum']
            writer = csv.DictWriter(invoice, fieldnames=fieldnames)
            for item in self.basket.values():
                writer.writerow({'category': item[0].strip(),
                                 'brand': item[1].strip(),
                                 'barcode': item[2].strip(),
                                 'number': item[3],
                                 'price of one product': item[4].strip(),
                                 'hole price': item[5],
                                 'totall sum': item[6]})
            writer.writerow({'totall sum': self.totallsum})

        # Updates inventory:
        for item in self.basket.values():
            file = open("product.csv", 'r')
            file_data = file.readlines()
            file.close()
            file_overwrite = open("product.csv", 'w')
            line_counter = 1
            for line in file_data:
                if line_counter > 1:
                    data = line.strip().split(",")
                    if data[2].strip() == item[2].strip():
                        newstock = int(data[4]) - int(item[3])
                        data[4] = str(newstock)
                        newdata = ','.join(data)
                        file_overwrite.write(newdata + '\n')
                    else:
                        newdata = ','.join(data)
                        file_overwrite.write(newdata + '\n')
                else:
                    file_overwrite.write(line)
                line_counter += 1
            file_overwrite.close()
