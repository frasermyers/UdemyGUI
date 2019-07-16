from tkinter import *

root = Tk()

label_1 = Label(root, text="Name: ")
label_1.grid(row=0, column=0, sticky=E)

label_2 = Label(root, text="Password: ")
label_2.grid(row=1, column=0, sticky=E)

entry_space = Entry(root)
entry_space.grid(row=0, column=1)

entry_space_2 = Entry(root)
entry_space_2.grid(row=1, column=1)

check_button = Checkbutton(root, text="Remember Password")
check_button.grid(columnspan=2)

root.mainloop()