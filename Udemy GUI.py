from tkinter import *

root = Tk()


def print_name(event):
    print("Hello there Fraser Myers")


def rude_name(event):
    print("Cunt")


button_1 = Button(root, text="Click Me")
button_1.bind("<Button-1>", print_name)
button_1.bind("<Button-3>", rude_name)
button_1.pack()

root.mainloop()