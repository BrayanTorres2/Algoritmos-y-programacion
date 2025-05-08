
import turtle 

t = turtle.Turtle()  
  
turtle.bgcolor("black")  
turtle.pensize(2)  
turtle.speed(0)  
  
for i in range(6):  
    for colors in ["purple", "aqua", "magenta", "green", "lime", "white"]:  
        turtle.color(colors)  
        turtle.circle(100)  
        turtle.left(10)  

turtle.speed(10)
turtle.pensize(10)

def curveMove():
  for i in range(200):
    turtle.rt(1)
    turtle.fd(1)

t=turtle.Turtle()
#N
t.speed(3)
t.shape("circle")
t.color("aqua")
t.pensize(35)
t.penup()
t.goto(-450,-90)
t.pendown()
t.lt(90)
t.fd(140)
t.rt(145)
t.fd(170)
t.lt(145)
t.fd(140)

#A
t.color("lime")
t.penup()
t.goto(-300,-90)
t.pendown()
t.rt(25)
t.fd(150)
t.rt(130)
t.fd(150)
t.penup()
t.lt(160)
t.fd(40)
t.lt(85)
t.fd(15)
t.pendown()
t.fd(90)

#T
t.color("purple")
t.penup()
t.goto(-100,-90)
t.pendown()
t.rt(90)
t.fd(140)
t.rt(90)
t.bk(45)
t.fd(90)

#A
t.color("black")
t.penup()
t.goto(-50,-90)
t.pendown()
t.lt(90)
t.rt(25)
t.fd(150)
t.rt(130)
t.fd(150)
t.penup()
t.lt(160)
t.fd(40)
t.lt(85)
t.fd(15)
t.pendown()
t.fd(90)

#L
t.color("aqua")
t.penup()
t.goto(125,50)
t.pendown()
t.rt(-90)
t.fd(140)
t.lt(90)
t.fd(90)

#I
t.color("lime")
t.penup()
t.goto(275,-90)
t.pendown()
t.lt(90)
t.fd(140)

#A
t.color("purple")
t.penup()
t.goto(325,-90)
t.pendown()
t.rt(25)
t.fd(150)
t.rt(130)
t.fd(150)
t.penup()
t.lt(160)
t.fd(40)
t.lt(85)
t.fd(15)
t.pendown()
t.fd(90)

turtle.done()
