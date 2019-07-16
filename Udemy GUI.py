from tkinter import *

root = Tk()

label_1 = Label(root, text="Enter your expression!")
label_1.pack()


def evaluate(event):
    data = e.get()
    answer.configure(text="Answer: " + str(eval(data)))


e = Entry(root)

e.bind("<Return>", evaluate)
e.pack()

answer = Label(root)
answer.pack()


root.mainloop()