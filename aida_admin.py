import csv

"""save admin info in text file"""
file_path = "admin info.txt"
file = open(file_path, "w+")
file.write("username," + str(hash("admin")) + ",password," + str(hash("0000")) + ",end")


class Admin:
    def __init__(self, user_name=hash("admin"), password=hash("0000")):
        self.name = user_name  # the user name by default is admin
        self.password = password  # the password by default is 0000

    def login(self, user, pas):
        """admin must login to the program """
        if user == self.name and pas == self.password:
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
