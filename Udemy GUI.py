from tkinter import *

root = Tk()

equa = "0"

equation = StringVar()

calculation = Label(root, textvariable=equation)

equation.set("23+54")

calculation.grid(columnspan=4)


def btn_press(num):
      global equa
      equa += str(num)
      equation.set(equa)


button_0 = Button(root, text="0", command=lambda: btn_press(0))
button_0.grid(row=1, column=0)
button_1 = Button(root, text="1", command=lambda: btn_press(1))
button_1.grid(row=1, column=1)
button_2 = Button(root, text="2", command=lambda: btn_press(2))
button_2.grid(row=1, column=2)



root.mainloop()
