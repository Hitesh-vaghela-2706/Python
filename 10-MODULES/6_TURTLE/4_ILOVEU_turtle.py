import turtle
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('blue')
t.pensize(3)
def draw(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

# i write
draw(-300,300)
t.forward(200)
t.back(100)
t.right(90)
t.forward(200)
t.left(90)
t.forward(100)
t.backward(200)

# heart
t.pensize(3)
draw(0,100)
t.fillcolor('red')
t.begin_fill()
t.left(45)
t.forward(142.857) # X/1.4 of X
t.circle(64.143,180) # 40% of 200
t.right(90)
t.circle(64.143,180)
t.right(7)
t.forward(135.67)
t.end_fill()


# u writing
draw(130,300)
t.right(38) # 45-7
t.forward(170)
t.circle(30,65) 
t.left(25) # 65+25=90
t.forward(170)
t.circle(30,65)
t.left(25)
t.forward(190)

turtle.done()
