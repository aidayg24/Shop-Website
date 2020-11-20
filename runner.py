from tkinter import *  # importing tkinter library
from tkinter import ttk
from tkinter import messagebox
from admin import Admin

admin=Admin()


def about():
    messagebox.showinfo("about maktab store",
                        "Project 4: Store Accounting\nprogramming by:\ntahere zare(raha),aida rostami,malihe mirzaii")


store = Tk()  # making a window for the home page of the shop
store.title('maktab store')
store.minsize(500, 500)
store.maxsize(1600, 1200)
store.geometry('800x600')
store.menubar = Menu(store)
store.helpmenu = Menu(store.menubar, tearoff=0)
store.helpmenu.add_command(label="About", command=about)
store.menubar.add_cascade(label="Help", menu=store.helpmenu)
store.config(menu=store.menubar)  # display the menu
scrollbar = Scrollbar(store)

store.rowconfigure(0, minsize=800, weight=1)

store.columnconfigure(1, minsize=800, weight=1)

taskbar_frame = Frame(store, relief=RAISED, bd=2, bg='grey')
btn_admin = Button(taskbar_frame, text='Admin', bg='firebrick4', command=admin.login).grid(row=0, column=0,
                                                                                            sticky="ew", padx=5, pady=5)
btn_search = Button(taskbar_frame, text='Search', bg='VioletRed4').grid(row=1, column=0,
                                                                                                    sticky="ew", padx=5,
                                                                                                    pady=5)
btn_cart = Button(taskbar_frame, text='Cart', bg='VioletRed4').grid(row=2, column=0,
                                                                                                sticky="ew", padx=5,
                                                                                                pady=5)
btn_exit = Button(taskbar_frame, text="Exit", bg='red4', command=store.quit).grid(row=10, column=0, sticky="ew", padx=5)
taskbar_frame.grid(row=0, column=0, sticky="ns")

fr_main = Frame(store, relief=RAISED, bd=1)
lbl_welcome = Label(fr_main, text='Maktab store\n\n', fg='black', font=('Garamond', 20))
file = open("product.csv", 'r')
row=3

for line in file.readlines():
    print(line)
    data = line.strip().split(",")
    show=Label(fr_main, text='{}    {}    {}'.format(data[0] , data[1] , data[3] )+ "\n")
    show.grid(row=row,column=0, sticky="w", padx=5, pady=5)
    print(show)
    row+=1
file.close()
lbl_welcome.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
fr_main.grid(row=0, column=1, sticky="nsew")

store.mainloop()  # creating a loop for the main window to store the changes