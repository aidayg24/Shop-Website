import csv
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

    def login(self, pas):
        """admin must login to the program """
        my_pass = str(pas).encode()
        hash_my_pass = hashlib.md5(my_pass).hexdigest()
        if hash_my_pass == self.password:
            ###in main : print("login was successful.")
            logger.info("admin log in!")
            return True
        else:
            ###in main :print("your password or user name was not correct")
            ###in main we can manage if the password is wrong or the user name
            logger.warning("login failed")
            return False

    def change_info(self, pas):
        """the admin can change the user name and password"""
        ###we must have an item in main to change info !
        new_pass = str(pas).encode()
        hash_new_pass = hashlib.md5(new_pass).hexdigest()
        file = open("admin info.txt", "w+")
        file.write("password," + str(hash_new_pass))
        file.close()
        logger.info("change info successfully")
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
            logger.info("new product added")

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

    def show_invoices(self):
        """admin can see the previous invoices by this method"""
        ###get info from customer !!!write this after customer modole
        pass

    def __str__(self):
        pass
