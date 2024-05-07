import turtle
A = ('green','yellow')
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('black')
t.pencolor('white')
t.speed(0)
c = 0
d = 0
while True:
    for i in range(4):
        t.color(A[i%2])
        t.forward(80)
        t.right(90)
    t.right(5)
    c+= 1
    if c>=360/5:
        t.right(30)
        t.forward(50)
        c = 0
        d+=1
        if d>=12:
            break
turtle.done()