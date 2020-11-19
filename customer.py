class Customer:
    def __init__(self, basket, invoice, final_price):
        self.basket = basket
        self.invoice = invoice
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
