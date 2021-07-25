import turtle
import time

turtle.bgcolor('black')
turtle.pensize(2)
turtle.speed(0)
turtle.pencolor('green')
turtle.penup()

turtle.goto(0,200)
turtle.pendown()

a = 0
b = 0

while True:
    turtle.forward(a)
    turtle.right(b)
    a = a+3
    b = b+1
    if b ==220:
        time.sleep(3)
        break
