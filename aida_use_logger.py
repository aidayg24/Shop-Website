import logging

LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename="logfile.log",
                    level=logging.DEBUG,
                    format=LOG_FORMAT,
                    filemode='a')


logger = logging.getLogger()
###in main :when admin log in successfully:
logger.info("admin login!")
###in main :when login failde:
logger.warning("login failed")
###in main: whem admin change info:
logger.info("info changed")
###in main : when a new product added:
logger.info("admin added new product")
###in main : when customer  buy things:
logger.info("new invoices ")
###in main :when the stock of a product is 0:
logger.warning("stock of "+"product name" +"= 0")
###in main :for exeptions:
logger.warning("exeption") #or it can be logger.debug