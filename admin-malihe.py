class Admin:

    def __init__(self):
        self.passw = hash(13741387)

    def check_pass(self, ramz=None):
        while self.passw != ramz:
            ramz = hash(int(input("enter your password: ")))
            if self.passw == ramz:
                print("The password is correct")
                new_ramz = input("Do you want to change the password for more security?(yes/no) ")
                if new_ramz == "yes":
                    self.passw = hash(input("Enter the new password: "))
                    print("Password changed")
                    break
                elif new_ramz == "no":
                    break
            else:
                print("Wrong password. Try again")

    def list_items(self,MainList):
        f = open("Products.txt", "r")
        i = 1
        for line in f:
            date = line.split()
            MainList.append(date)
            print(str(i) + " " + line)
            i = i + 1
        if len(MainList) == 0:
            print("There is no case")

    def add_item(self,MainList):
        ans = "yes"
        while ans == "yes":
            barcode = input("Please enter the barcode")
            name = input("Please enter the name: ")
            brand = input("Please enter the brand: ")
            count = input("Please count : ")
            price = input("Please Price the brand: ")
            f = open("Products.txt", "a")
            line1 = barcode + " " + name + " " + brand + " " + count + " " + price
            print("Product added : " + line1)
            MainList.append(line1.split())
            f.writelines( barcode + " " + name + " " + brand + " " + count + " " + price )
            ans = input("Do you want to import another product?(yes/no)")
            f.close()

    def update_item(self,MainList):
        ans = "yes"
        while ans == "yes":
            f = open("Products.txt", "r")
            for line in f:
                date = line.split()
                MainList.append(date)
            barcode = input("Please enter the barcode")
            f = open("Products.txt", "r")
            for line in f:
                date = line.split()
                MainList.append(date)
            for i in MainList:
                if barcode == i[0]:
                    numitem = int(input("The product is available. How many should be added? "))
                    i[3] = int(i[3]) + numitem
                    print("Product added" + str(i[0]) + " " + str(i[1]) + " " + str(i[2]) + " " + str(i[3]) + " " + str(
                        i[4]))
                    break
            ans = input("Do you want to import another product?(yes/no)")

    def factor(self):
        pass

    def warning(self):
        pass

