import turtle as t
import colorsys

t.bgcolor('black')
t.tracer(100)
t.pensize(1)
h=0.5

for i in range(250):
    c = colorsys.hsv_to_rgb(h,1,1)
    h = 0.0008
    t.fillcolor(c)
    t.fd(i)
    t.lt(100)
    t.circle(30)
    for j in range(2):
        t.fd(i*j)
        t.rt(109)
    t.end_fill()


import turtle as tur
import colorsys as cs

tur.setup(800,800)
tur.speed(0)
tur.tracer(10)
tur.width(2)
tur.bgcolor("Black")

for j in range(25):
    for i in range(25):
        tur.color(cs.hsv_to_rgb(i/15,j/25,1))
        tur.right(90)
        tur.circle(200-j*4,90)
        tur.left(90)
        tur.circle(200-j*4,90)
        tur.right(180)
        tur.circle(50,24)

    tur.hideturtle()
    tur.done()

import turtle
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.pencolor("green")
a = 0
b = 0
t.speed(0)
t.penup()
t.goto(0,200)
t.pendown()

while True:
    t.forward(a)
    t.right(b)
    a+=3
    b+=1
    if b == 210:
        break