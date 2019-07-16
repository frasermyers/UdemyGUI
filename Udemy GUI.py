from tkinter import *
import random

root = Tk()

canvas = Canvas(root, width=300, height=300)
canvas.pack()


canvas.create_text(150, 200, text="This is gay", fill='blue', font=("Times", 30))


root.mainloop()