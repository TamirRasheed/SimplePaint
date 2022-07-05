import turtle
import colorsys

t = turtle.Turtle()
turtle.tracer(3)
turtle.Screen().bgcolor("black")

t.pensize(1)
t.speed()

n = 36
h = 0
t.goto(-60,0)

for i in range(200):
    c = colorsys.hsv_to_rgb(h,1,0.9)
    t.pencolor(c)
    t.circle(105,103)
    t.backward(98)
    t.right(60)
    t.circle(70,68)
    t.left(87)
    t.backward(108)
    t.forward(150)
    h+=1/n
turtle.done()