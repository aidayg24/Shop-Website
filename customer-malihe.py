class Customer:
    summ = 0
    list2 = []

    def list_items(self, MainList):
        print(MainList)
        i = 1
        for line in MainList:
            print(str(i) + " " + MainList[1] + " " + MainList[2] + " " + MainList[4])
            i = i + 1

    def select_items(self, MainList):
        customernum = 0
        while customernum != "finish":
            f = open("Products.txt", "r")
            for line in f:
                date = line.split()
                MainList.append(date)
            customernum = input("Enter the desired product number (Enter the finish to complete the purchase)\n")
            if customernum != "finish":
                if MainList[int(customernum) - 1][3] == "0":
                    print("Your desired product is finished")
                else:
                    print("**Product added to your cart**")
                    MainList[int(customernum) - 1][3] = str(int(MainList[int(customernum) - 1][3]) - 1)
                    f = open("Products.txt", "r")
                    listt = [None]
                    for line in f:
                        datte = line.split()
                        listt.append(datte)
                        if len(listt) == int(customernum) + 1:
                            self.list2.append(listt[int(customernum)])
                            self.summ += int(listt[int(customernum)][4])

    def invoice(self):
        a = 1
        print(" Products purchased")
        for i in self.list2:
            print(str(a) + " " + i[1] + " " + i[2] + " " + i[4] + "\n")
            a = a + 1
        print("Amount of money That had to be paid :" + str(self.summ) + "\n")
