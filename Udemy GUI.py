from tkinter import *

root = Tk()

top_frame = Frame(root)
top_frame.pack()

bot_frame = Frame(root)
bot_frame.pack(side=BOTTOM)

button_one = Button(top_frame, text="Click Me!", fg="Blue")
button_one.pack(side=LEFT)

button_two = Button(bot_frame, text="Hello", fg="Red")
button_two.pack(side=LEFT)

button_three = Button(bot_frame, text="Hello", fg="Purple")
button_three.pack(side=LEFT)

button_four = Button(top_frame, text="Hello", fg="Yellow")
button_four.pack(side=LEFT)

root.mainloop()