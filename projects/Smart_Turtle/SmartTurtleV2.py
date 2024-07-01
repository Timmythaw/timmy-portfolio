# Onclick Draw
import turtle
import random

colors = ["#72447A", "#BD597E", "#F27F70",
          "#FFB761", "#F9F871", "#00C6C1", "#FFF7D6"]

tim = turtle.Turtle()
scr = turtle.Screen()
scr.bgcolor("#21325E")
scr.title("Click on any Place on the Screen!")
tim.shape("turtle")
tim.speed(0.3)
tim.hideturtle()


def triangle():
    length = random.randrange(30, 80)
    repeat = random.randint(0, 11)
    for i in range(repeat):
        outColors = random.randrange(0, len(colors))
        tim.color(colors[outColors])
        for i in range(3):
            tim.forward(length)
            tim.left(120)
        # 10 Times repeating = 36 degrees * 10 = 360 degrees
        tim.left(360/repeat)


def square():
    length = random.randrange(30, 50)
    repeat = random.randint(0, 11)
    for i in range(repeat):
        outColors = random.randrange(0, len(colors))
        tim.color(colors[outColors])
        for i in range(4):
            tim.forward(length)
            tim.left(90)
        tim.left(360/repeat)


def octagon():
    length = random.randrange(10, 30)
    repeat = random.randint(0, 11)
    for i in range(repeat):
        outColors = random.randrange(0, len(colors))
        tim.color(colors[outColors])
        for i in range(8):
            tim.forward(length)
            tim.left(45)
        tim.left(360/repeat)


def circle():
    radius = random.randrange(30, 50)
    repeat = random.randint(0, 11)
    for i in range(repeat):
        outColors = random.randrange(0, len(colors))
        tim.color(colors[outColors])
        for i in range(8):
            tim.circle(radius)
        tim.left(360/repeat)


def star():
    length = random.randrange(50, 80)
    repeat = random.randint(0, 11)
    for i in range(repeat):
        outColors = random.randrange(0, len(colors))
        tim.color(colors[outColors])
        for i in range(5):
            tim.forward(length)
            tim.left(144)
        tim.left(360/repeat)


def rhombus():
    length = random.randrange(30, 80)
    repeat = random.randint(0, 11)
    for i in range(repeat):
        outColors = random.randrange(0, len(colors))
        tim.color(colors[outColors])
        for i in range(2):
            tim.forward(length)
            tim.left(60)
            tim.forward(length)
            tim.left(120)
        tim.left(360/repeat)


def draw(x, y):
    penSize = random.randrange(2, 4)
    tim.pensize(penSize)
    tim.penup()
    tim.goto(x, y)
    tim.pendown()
    shape = random.choice(
        ["triangle", "octagon", "circle", "square", "star", "rhombus"])
    if shape == "triangle":
        triangle()

    elif shape == "ocatgon":
        octagon()

    elif shape == "circle":
        circle()

    elif shape == "square":
        square()

    elif shape == "star":
        star()

    elif shape == "rhombus":
        rhombus


def reset(x, y):
    tim.clear()

# Function to kill the program


def stop():
    turtle.bye()

# All the functions tgt


def main():
    turtle.listen()
    turtle.onscreenclick(draw, 1)  # 1 = left Click , #3 = right Click
    turtle.onscreenclick(reset, 3)
    turtle.onkeypress(stop, "Escape")
    turtle.mainloop()


main()
