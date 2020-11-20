###***aida's comments

class Admin:

    def __init__(self):
        self.passw = hash(13741387)
        ###***dont use this method of hash . this will gives you alot of errors! use hashlib
        ###***this library is better for hashing. read my aida_admin code I use this in my code.

    def check_pass(self, ramz=None):###*** please replace "ramz" with "password" and do not use fingilish in your code!
        ###*** this while code is a great idea we can use this and it give admin the oppertunaty to
        ###***try several times for give the password to system!
        while self.passw != ramz:
            ramz = hash(int(input("enter your password: "))) ###***again the hash is not ok!
            if self.passw == ramz:
                print("The password is correct")
                new_ramz = input("Do you want to change the password for more security?(yes/no) ")
                ###*** you could design an other method for change informations it would be better in my oppinion
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
        ###*** I think working with txt files in this case is not the best idea.I used csv in my code
        i = 1
        for line in f:
            date = line.split()###*** it would be better to use .strip().split() in this case
            MainList.append(date)
            print(str(i) + " " + line)
            i = i + 1
        if len(MainList) == 0:
            print("There is no case")

    def add_item(self,MainList):
        ans = "yes"
        ###***what is ans?? you did not have this before in your code!
        while ans == "yes":
            barcode = input("Please enter the barcode")
            name = input("Please enter the name: ")
            brand = input("Please enter the brand: ")
            count = input("Please count : ")
            price = input("Please Price the brand: ")
            f = open("Products.txt", "a")
            line1 = barcode + " " + name + " " + brand + " " + count + " " + price
            print("Product added : " + line1)
            ###***why you print this?there is no need for this
            MainList.append(line1.split())
            f.writelines( barcode + " " + name + " " + brand + " " + count + " " + price )
            ###*** you could jast write f.write(line1)
            ans = input("Do you want to import another product?(yes/no)")
            ###***its somehow confusing you could give ans as an arguman to function
            f.close()

    def update_item(self,MainList):
        ans = "yes"
        ###***again same comment for ans!
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

