import turtle

def petal(t, radius, angle):
    for i in range(2):
        t.circle(radius, angle)
        t.left(180 - angle)
        
def flower(t, n, radius, angle):
    for i in range(n):
        petal(t, radius, angle)
        t.left(360.0 / n)
        
def move(t, length):
    window = turtle.Screen()
    window.bgcolor("Yellow")
    t.pu()
    t.fd(length)
    t.pd()
    
anms = turtle.Turtle()
anms.speed(100)

anms.color("green")
anms.shape("turtle")
move(anms, -150)
anms.begin_fill()
flower(anms, 7, 60.0, 60.0)
anms.end_fill()

anms.color("red")
move(anms, 150)
anms.begin_fill()
flower(anms, 10, 30.0, 70.0)
anms.end_fill()

anms.color("blue")
move(anms, 150)
anms.begin_fill()
flower(anms, 14, 70.0, 50.0)
anms.end_fill()

turtle.mainloop()