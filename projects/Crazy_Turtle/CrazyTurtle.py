import turtle
import random

colors = ["#72447A", "#BD597E", "#F27F70",
          "#FFB761", "#F9F871", "#00C6C1", "#FFF7D6"]

tur = turtle.Turtle()
scr = turtle.Screen()
scr.bgcolor("#21325E")
scr.title("Click on any Place on the Screen!")
tur.shape("turtle")
tur.speed(0.5)


def magic(x, y):
    while True:
        size = random.randrange(2, 4)
        repeatTime = random.randint(0, 21)
        numLines = random.randrange(1, 8)
        lenLines = random.randrange(20, 150)
        angTurn = random.randrange(1, 360)
        x = random.randrange(-250, 250)
        y = random.randrange(-250, 250)

        # use The random values
        tur.pensize(size)
        tur.penup()
        # set position randomly
        tur.setpos(x, y)
        tur.pendown()

    # Start Drawing
        for i in range(repeatTime):
            for i in range(numLines):
                outColors = random.randrange(0, len(colors))
                fillColors = random.randrange(0, len(colors))
                tur.color(colors[outColors], colors[fillColors])
                tur.forward(lenLines)
                tur.left(angTurn)
            tur.left(360/repeatTime)
        tur.hideturtle()


def pause(x, y):
    turtle.done()


def reset():
    tur.clear()


def stop():
    turtle.bye()


def main():
    turtle.listen()
    turtle.onscreenclick(magic, 1)
    turtle.onscreenclick(pause, 3)
    turtle.onkeypress(stop, "Escape")
    turtle.onkeypress(reset, "space")
    turtle.mainloop()


main()
