from tkinter import *

root = Tk()

button_one = Button(None, text="Click Me!", fg="Blue")
button_one.pack()

button_two = Button(None, text="Hello", fg="Red")
button_two.pack(fill=X)

button_three = Button(None, text="Hello", fg="Purple")
button_three.pack(side=RIGHT, fill=Y)

button_four = Button(None, text="Hello", fg="Yellow")
button_four.pack()

root.mainloop()