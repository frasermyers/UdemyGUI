from tkinter import *

root = Tk()

label_1 = Label(root, text="Name: ")
label_1.grid(row=0, column=0)

entry_space = Entry(root)
entry_space.grid(row=0, column=1)

check_button = Checkbutton(root, text="Remember Name")
check_button.grid(columnspan=2)

root.mainloop()