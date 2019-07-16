from tkinter import *

root = Tk()


def print_name():
    print("Hello there Fraser Myers")


button_1 = Button(root, text="Click Me", command=print_name)
button_1.pack()

root.mainloop()