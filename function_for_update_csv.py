import logging

open("logfile.log", 'a+')
logger = logging.getLogger()


def update_csv_data_stock():
    """ the function opens the csv file that contains the list of products
        and updates the stock(number of a product) after costumer buy something"""
    file = open("product.csv", 'r')
    file_data = file.readlines()
    file.close()
    product_name = input("product type:\n")
    brand = input("product brand\n")
    the_num = int(input("the number of products that costumer buy:\n"))
    file_overwrite = open("product.csv", 'w')
    for line in file_data:
        data = line.strip().split(",")
        if data[4] == 0:
            print("the stock of this product is  0. you have to charge this")
            logger.warning(data[0] + data[1] + "ends")

        if data[0] == product_name and data[1] == brand:
            stock = int(str(data[4]))
            if stock <= 10:
                logger.warning("charge the product")
            if stock < the_num:
                logger.warning("buy failed")
            else:
                stock -= the_num
                data[4] = str(stock)
            new_data = ",".join(data)
            file_overwrite.write(new_data + "\n")
        else:
            file_overwrite.write(line)
###you can yous this function in main when a customer buy something
###please show the admin a message when line 22 or 24 happends
