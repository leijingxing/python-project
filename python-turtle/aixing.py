import turtle
import time
def liujia():
	for i in range (200):
		turtle.right(1)
		turtle.forward(1)
turtle.speed(10)
turtle.bgcolor("pink")
turtle.color('red','pink')
turtle.pensize(5)
turtle.goto(0,0)
turtle.begin_fill()
turtle.left(140)
turtle.forward(112)
liujia()
turtle.left(120)
liujia()
turtle.forward(112)
turtle.end_fill()
turtle.up()
turtle.goto(100,-10)
turtle.write("I Love you")
turtle.penup()
turtle.goto(100,-30)
turtle.pendown()

turtle.penup()
turtle.goto(100,-50)
turtle.pendown()
turtle.write("Love")
turtle.penup()
turtle.home()
turtle.done()