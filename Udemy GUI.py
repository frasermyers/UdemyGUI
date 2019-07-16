from tkinter import *

root = Tk()

label_1 = Label(root, text="Label 1")
label_1.grid(row=0, column=0)

label_2 = Label(root, text="Label 2")
label_2.grid(row=0, column=1)

label_3 = Label(root, text="Label 3")
label_3.grid(row=1, column=0)

root.mainloop()