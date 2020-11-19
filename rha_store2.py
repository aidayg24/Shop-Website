from tkinter import *  # importing tkinter library
from tkinter import messagebox
from tkinter import ttk





def loggingadmin(self):
    self.logadmin = Tk()

    self.password = Entry(self, width=30)  # making the entry for password (==input)
    self.password.config(show='*')
    self.lblpassword = ttk.Label(text="Your Password : ",
                                 font=('Garamond', 16))  # making a label for password entry
    self.lblpassword.grid(row=1, column=0, sticky='W', pady=10)
    self.password.grid(row=1, column=1, sticky=W)
    self.chvar = IntVar()
    self.chvar.set(0)
    Button(self, text="sign in", bg='yellow', command=self.sign_in).pack()

    pass


def loggingcustomer():
    pass


def sreach_merchandise():
    pass


store = StoreWindow()  # making a window for the home page of the shop

store.rowconfigure(0, minsize=800, weight=1)
store.columnconfigure(1, minsize=800, weight=1)

taskbar_frame = Frame(store, relief=RAISED, bd=2, bg='grey')
btn_admin = Button(taskbar_frame, text='Admin', bg='firebrick4', command=loggingadmin).grid(row=0, column=0,
                                                                                            sticky="ew", padx=5, pady=5)
btn_search = Button(taskbar_frame, text='Search', bg='VioletRed4', command=sreach_merchandise).grid(row=1, column=0,
                                                                                                    sticky="ew", padx=5,
                                                                                                    pady=5)
btn_cart = Button(taskbar_frame, text='Cart', bg='VioletRed4', command=sreach_merchandise).grid(row=2, column=0,
                                                                                                sticky="ew", padx=5,
                                                                                                pady=5)
btn_exit = Button(taskbar_frame, text="Exit", bg='red4', command=store.quit).grid(row=10, column=0, sticky="ew", padx=5)
taskbar_frame.grid(row=0, column=0, sticky="ns")

fr_main = Frame(store, relief=RAISED, bd=1)
lbl_welcome = Label(fr_main, text='Maktab store\n\n', fg='black', font=('Garamond', 20))
# lbl_user = Label(fr_main, text='For what purpose do you want to enter the store?\n\n', font=('Garamond', 16))
# # btn_admin = Button(fr_main, text='Admin', bg='purple', font=('Garamond', 16), width=30, bd=5, command=loggingadmin)
# btn_customer = Button(fr_main, text='Customer', bg='purple', font=('Garamond', 16), width=30, bd=5,
#                       command=loggingcustomer)
lbl_welcome.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
# lbl_user.grid(row=3, column=4, sticky="ew", padx=5)
# #btn_admin.grid(row=4, column=4, sticky="ew", padx=5)
# btn_customer.grid(row=5, column=4, sticky="ew", padx=5)
fr_main.grid(row=0, column=1, sticky="nsew")

store.mainloop()  # creating a loop for the main window to store the changes
