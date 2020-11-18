class Admin:
    list1 = []

    def __init__(self):
        self.passw = hash(13741387)

    def check_pass(self, ramz=None):
        while self.passw != ramz:
            ramz = hash(int(input("ramz vared kon")))
            if self.passw == ramz:
                print("ok")
                new_ramz = input("behtar baraye amniat ramzeto avaz koni?yes/no")
                if new_ramz == "yes":
                    self.passw = hash(input("ramz jadid vRED KON"))
                    print("ramz avaz shod")
                    break
                elif new_ramz == "no":
                    break
            else:
                print("ramz eshtabah dobre talah kon")

    def list_items(self):
        f = open("demofile2.txt", "r")
        i = 1
        for line in f:
            date = line.split()
            self.list1.append(date)
            print(str(i) + " " + line)
            i = i + 1
        print(self.list1)

    def add_item(self):
        print(self.list1)
        ans = "yes"
        while ans == "yes":
            barcode = input("lotfan barcod vared konid")
            for i in self.list1:
                if barcode == i[0] and ans=="yes":
                    num_item = int(input("kalaee k mikhay vared koni mojode che tedadi mikhay ezafe koni?"))
                    i[3] = int(i[3]) + num_item
                    print(i)
                    print(
                        "kala ezafe shod" + str(i[0]) + " " + str(i[1]) + " " + str(i[2]) + " " + str(i[3]) + " " + str(
                            i[4]))
                    ans = input("Do you want to import another product?(yes/no")
                    break

                elif ans == "yes":
                    name = input("lotfan name vared konid")
                    brand = input("lotfan brand vared konid")
                    tedad = input("lotfan tedad vared konid")
                    gheymat = input("lotfan gheymat vared konid")
                    f = open("demofile2.txt", "a")
                    line1 = barcode + " " + name + " " + brand + " " + tedad + " " + gheymat
                    print("kala ezafe shod=  " + line1)
                    self.list1.append(line1.split())
                    f.writelines("\n" + barcode + " " + name + " " + brand + " " + tedad + " " + gheymat + "\n")
                    ans = input("Do you want to import another product?(yes/no)")
                    f.close()

    def factor(self):
        pass

    def warning(self):
        pass
# [['1374', 'name1', 'brand1', 'tedad1', '24000'], ['1375', 'name2', 'brand2', 'tedad2', '25000'], ['1376', 'name3', 'brand3', 'tedad3', '26000']]
