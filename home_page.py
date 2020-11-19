def show_page_to_admin():
    """this function is for reading data from csv and
    show items to admin in home page of website"""
    file = open("product.csv", 'r')
    for line in file.readlines():
        data = line.strip().split(",")
        show = "category: " + data[0] + " brand: " + data[1] + " barcode: " + data[2] + \
               " price: " + data[3] + " stock: " + data[4] + "\n"
        return show


def show_page_to_customer():
    """this function is for reading data from csv and
        show items to customer in home page of website"""
    file = open("product.csv", 'r')
    for line in file.readlines():
        data = line.strip().split(",")
        show = "category: " + data[0] + " brand: " + data[1] + " price: " + data[3] + "\n"
        return show
