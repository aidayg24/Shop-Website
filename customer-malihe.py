class Customer:
    list2 = []
    summ = 0

    def list_items(self):
        f = open("demofile2.txt", "r")
        i = 1
        for line in f:
            date = line.split()
            print(str(i) + " " + date[1] + " " + date[2] + " " + date[4])
            i = i + 1

    def select_items(self):
        moshtari = 0
        # summ = 0
        while moshtari != "finish":
            moshtari = input("shomare mored nazar ra vared konid")
            if moshtari == "finish":
                print("Amount of money That had to be paid" + str(self.summ))
                print(self.list2)
                break
            f = open("demofile2.txt", "r")
            listt = [None]
            for line in f:
                datte = line.split()
                listt.append(datte)
                # print(listt)
                # print(moshtari)
                if len(listt) == int(moshtari) + 1:
                    self.list2.append(listt[int(moshtari)])
                    # print(listt[int(moshtari)][4])
                    self.summ += int(listt[int(moshtari)][4])

    def invoice(self):
        a = 1
        for i in self.list2:
            print(str(a) +" "+ i[1] +" "+ i[2] + " "+i[4] + "\n")
            a = a + 1
        print("mablagh kol pardakhti="+str(self.summ))

# from customer import Customer
# b=Customer()
# b.select_items()
