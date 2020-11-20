import csv


class Customer:
    def __init__(self, final_price=0, basket={}):
        self.basket = basket
        self.price = final_price

    @staticmethod
    def search(category, brand):
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

    def buy(self, barcode, number):  # number is the amount of product that customer wants
        """the customer selects an item to buy and add that to the basket """
        file = open("product.csv", 'r')
        for line in file.readlines():
            data = line.strip().split(",")
            if data[2] == barcode:
                the_price_of_one = int(data[3])
                self.basket[barcode] = ("category: " + data[0] + " brand: " + data[1] +
                                        " barcode: " + data[2] + " price of one: " + data[3] +
                                        " total: " + str(the_price_of_one * number))
                self.price += (the_price_of_one * number)

    def remove(self, barcode):
        """the customer can remove an item from the basket
         before he or she get the final invoice. this function can not
         edit the number of the product that customer buy but can remove that
         item from basket"""
        for item in self.basket.keys():
            if item == barcode:
                del self.basket[barcode]

    def add_to_invoice(self):
        """this method records the final items in basket
        and gives an invoice and the price to
        customer and updates the entrepot """
        with open('invoice.csv', 'a', newline='') as invoice:
            fieldnames = ['category', 'brand', 'barcode', 'price of one product', 'hole price']
            writer = csv.DictWriter(invoice, fieldnames=fieldnames)
            for item in self.basket.keys():
                new_data = str(self.basket[item]).strip().split(" ")
                writer.writerow({'category': new_data[1],
                                 'brand': new_data[3],
                                 'barcode': new_data[5],
                                 'price of one product': new_data[7],
                                 'hole price': new_data[9]})
            writer.writerow({'category': "\n",
                             'brand': "\n",
                             'barcode': "\n",
                             'price of one product': "\n",
                             'hole price': "\n"})

    def show_invoice_to_customer(self):
        """this function show the final invoice to customer"""
        for item in self.basket.keys():
            print(self.basket[item])

