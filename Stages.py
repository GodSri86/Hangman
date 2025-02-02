from time import sleep
import turtle


def ResetPosition():
    turtle.penup()
    turtle.goto(0, 100)
    turtle.pendown()


def stages(tries):
    window = turtle.Screen()
    window.bgpic("turtle_background.png")
    window.setup(width=600, height=600, startx=-1, starty=-1)
    window.cv._rootwindow.resizable(False, False)
    window.cv._rootwindow.attributes("-topmost", True)
    turtle.pensize(15)
    if tries == 0:
        turtle.clear()
        global running
        ResetPosition()
        turtle.circle(50)
        turtle.right(45)
        turtle.forward(150)
        turtle.backward(150)
        turtle.right(90)
        turtle.forward(150)
        turtle.backward(150)
        turtle.left(45)
        turtle.forward(200)
        turtle.right(45)
        turtle.forward(100)
        turtle.backward(100)
        turtle.left(90)
        turtle.forward(100)
        sleep(2)
        turtle.reset()
    elif tries == 1:
        turtle.clear()
        global running
        ResetPosition()
        turtle.circle(50)
        turtle.right(45)
        turtle.forward(150)
        turtle.backward(150)
        turtle.right(90)
        turtle.forward(150)
        turtle.backward(150)
        turtle.left(45)
        turtle.forward(200)
        turtle.right(45)
        turtle.forward(100)
        sleep(2)
        turtle.reset()
    elif tries == 2:
        turtle.clear()
        global running
        ResetPosition()
        turtle.circle(50)
        turtle.right(45)
        turtle.forward(150)
        turtle.backward(150)
        turtle.right(90)
        turtle.forward(150)
        turtle.backward(150)
        turtle.left(45)
        turtle.forward(200)
        sleep(2)
        turtle.reset()
    elif tries == 3:
        turtle.clear()
        global running
        ResetPosition()
        turtle.circle(50)
        turtle.right(45)
        turtle.forward(150)
        turtle.backward(150)
        turtle.right(45)
        turtle.forward(150)
        sleep(2)
        turtle.reset()
    elif tries == 4:
        turtle.clear()
        global running
        ResetPosition()
        turtle.circle(50)
        turtle.right(90)
        turtle.forward(150)
        sleep(2)
        turtle.reset()
    elif tries == 5:
        turtle.clear()
        global running
        ResetPosition()
        turtle.circle(50)
        sleep(2)
        turtle.reset()
    elif tries == 100:
        turtle.clear()
        global running
        ResetPosition()
        style = ('Courier', 20, 'italic')
        turtle.write('HANGMAN!', font=style, align='center')
        turtle.reset()
