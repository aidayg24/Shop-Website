from tkinter import *


# inherianceing from Tk module and initializing the Tk class for creating object
class Store(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title('maktab store')

        self.menubar = Menu(self)  # create a toplevel menu
        self.filemenu = Menu(self.menubar, tearoff=0)  # create a pulldown menu, and add it to the menu bar
        self.filemenu.add_command(label="Exit", command=self.quit)
        self.menubar.add_cascade(label="File", menu=self.filemenu)
        self.helpmenu = Menu(self.menubar, tearoff=0)
        self.helpmenu.add_command(label="About", command=self.about)
        self.menubar.add_cascade(label="Help", menu=self.helpmenu)
        self.config(menu=self.menubar)# display the menu

        Label(self, text='\n\nWelcome to the maktab store\n\n', fg='blue', font=('nazanin', 22)).pack()
        Label(self, text='For what purpose do you want to enter the store?\n\n', font=('nazanin', 16)).pack()
        Button(self, text='Admin', bg='purple', font=('nazanin', 16), width=30, bd=5, command=self.loggingadmin).pack()
        Button(self, text='Customer', bg='purple', font=('nazanin', 16), width=30, bd=5,
               command=self.loggingcustomer).pack()

    def about(self):
        pass  # y panjre massage bshe k ysri etelaat bde b karbar

    def loggingadmin(self):
        # making a label for password entry
        Label(self, text="Password", font=('nazanin', 16)).pack()
        self.password = Entry(self)  # making the entry for password (==input)
        self.password.pack()
        Button(self, text="sign in", bg='yellow', command=self.sign_in).pack()

        pass

    def sign_in(self):
        pass  # daryafte password v chk krdn vse vorod

    def loggingcustomer(self):
        pass


# creating the object of app for tk main window
if __name__ == "__main__":
    store = Store()
    store.geometry('1800x1200')  # size of store window
    store.mainloop()  #creating the loop for the program
