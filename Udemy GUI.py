from tkinter import *

root = Tk()

equa = ""

equation = StringVar()

calculation = Label(root, textvariable=equation)

equation.set("Enter your equation")

calculation.grid(columnspan=4)


def btn_press(num):
      global equa
      equa += str(num)
      equation.set(equa)


def equal_press():
      global equa
      total = eval(equa)
      equation.set(total)
      equa = ""


def clear():
      global equa
      equa=""
      equation.set("")


button_0 = Button(root, text="0", command=lambda: btn_press(0))
button_0.grid(row=4, column=1)
button_1 = Button(root, text="1", command=lambda: btn_press(1))
button_1.grid(row=1, column=0)
button_2 = Button(root, text="2", command=lambda: btn_press(2))
button_2.grid(row=1, column=1)
button_3 = Button(root, text="3", command=lambda: btn_press(3))
button_3.grid(row=1, column=2)
button_4 = Button(root, text="4", command=lambda: btn_press(4))
button_4.grid(row=2, column=0)
button_5 = Button(root, text="5", command=lambda: btn_press(5))
button_5.grid(row=2, column=1)
button_6 = Button(root, text="6", command=lambda: btn_press(6))
button_6.grid(row=2, column=2)
button_7 = Button(root, text="7", command=lambda: btn_press(7))
button_7.grid(row=3, column=0)
button_8 = Button(root, text="8", command=lambda: btn_press(8))
button_8.grid(row=3, column=1)
button_9 = Button(root, text="9", command=lambda: btn_press(9))
button_9.grid(row=3, column=2)

plus = Button(root, text="+", command=lambda: btn_press("+"))
plus.grid(row=1, column=3)
minus = Button(root, text="-", command=lambda: btn_press("-"))
minus.grid(row=2, column=3)
multiply = Button(root, text="*", command=lambda: btn_press("*"))
multiply.grid(row=3, column=3)
divide = Button(root, text="/", command=lambda: btn_press("/"))
divide.grid(row=4, column=3)
equal = Button(root, text="=", command=equal_press)
equal.grid(row=4, column=2)
clear = Button(root, text="C", command=clear)
clear.grid(row=4, column=0)


root.mainloop()
