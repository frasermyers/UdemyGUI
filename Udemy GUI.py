from tkinter import *
import tkinter.messagebox

root = Tk()

def random():
    print("This is a statement")


main_menu = Menu(root)
root.configure(menu=main_menu)

sub_menu_1 = Menu(main_menu)
sub_menu_2 = Menu(main_menu)


main_menu.add_cascade(label="File", menu=sub_menu_1)

sub_menu_1.add_command(label="Random Function", command=random)
sub_menu_1.add_command(label="New File", command=random)
sub_menu_1.add_separator()
sub_menu_1.add_command(label="Poo", command=random)

main_menu.add_cascade(label="Edit", menu=sub_menu_2)


root.mainloop()
