import turtle
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('blue')
A = 0
B = 0
t.fillcolor("yellow")
t.begin_fill()
for i in range(200):
    t.left(59)
    t.forward(100)
    t.right(24)
    t.backward(50)
    A += 2
    B +=2
t.end_fill()
turtle.done()
