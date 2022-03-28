import colorsys
import turtle
colors=["red", "purple", "#03ffd5", "#08ff39", "#ff03a2", "yellow"]
t=turtle.Pen()
turtle.bgcolor("black")
t.speed(0)
i = 0
while(True):
    i=i+1
    t.pencolor(colors[i%6])
    t.width(i//100+1)
    t.forward(i)
    t.left(59)