from tkinter import *
import tkinter.messagebox

root = Tk()

tkinter.messagebox.showinfo("Window Title", "Did you know that the world just blew up?")

answer = tkinter.messagebox.askquestion("Question 1", "Are you human?")

if answer == "yes":
    tkinter.messagebox.showinfo("Congrats", "Thank god")

if answer == "no":
    tkinter.messagebox.showinfo("Alien", "You are 100% confirmed alien")


root.mainloop()