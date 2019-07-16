from tkinter import *

root = Tk()

canvas = Canvas(root, width=300, height=300)
canvas.pack()


def create_rect(x1, y1, x2, y2):
    canvas.create_rectangle(x1, y1, x2, y2, fill="blue")


create_rect(5, 50, 200, 70)
create_rect(5, 5, 240, 200)


root.mainloop()
