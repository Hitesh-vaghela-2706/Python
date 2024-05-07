import turtle
t = turtle.Turtle()
s = turtle.Screen()
s.title('hitesh')
s.bgcolor('gray')
t.speed(10)
A = 0
B = 0
for i in range(0,20):
    t.left(40)
    t.forward(A)
    t.right(260)
    t.forward(B)
    A += 3
    B += 2

C = 100
for i in range(20,100,5):
    t.circle(i,360)
    t.penup()
    t.goto(C,200)
    C = C - 1
    i = i + 5
    t.pendown()

turtle.done()