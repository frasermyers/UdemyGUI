from tkinter import *
import time

root = Tk()


def cum():

    canvas.create_rectangle(147, 100, 153, 80, fill='white')
    for j in range(0, 100):
        canvas.move(8, 0, -1)
        root.update()
        time.sleep(0.01)
        if j == 99:
            canvas.create_text(150, 70, text="Well done on losing your virginity", font=("Times", 16), fill="white")


def blue_balls():
    canvas.create_rectangle(120, 280, 140, 260, fill='blue')
    canvas.create_rectangle(160, 280, 180, 260, fill='blue')
    canvas.create_text(150, 70, text="You got blue balls", font=("Times", 20), fill="white")



def sex():
    canvas.create_rectangle(120, 280, 140, 260, fill='pink')
    canvas.create_rectangle(160, 280, 180, 260, fill='pink')
    canvas.create_rectangle(140, 100, 160, 260, fill='pink')

    canvas.create_polygon(100, 0, 140, 50, 140, 0, fill='pink')
    canvas.create_polygon(161, 0, 161, 50, 200, 0, fill='pink')

    canvas.create_line(150, 100, 150, 110, fill="purple")
    canvas.create_line(140, 120, 160, 120, fill="purple")

    jizz = Button(root, text="JIZZ", command=cum)
    jizz.pack()

    dont_jizz = Button(root, text="Don't Jizz", command=blue_balls)
    dont_jizz.pack()

    #for i in range(0, 60):
        #canvas.move(1, 0, -2)
        #canvas.move(2, 0, -2)
        #canvas.move(3, 0, -2)
       # root.update()
       # time.sleep(0.1)
       # if i == 59:
           # canvas.create_text(150, 150, text="Oh baby", font=("Times", 30)


canvas = Canvas(root, width=300, height=300, bg='black')
canvas.pack()

push = Button(root, text="Click here to have sex", command=sex)
push.pack()



root.mainloop()