import turtle
A = ('green','yellow')#num of col
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('black')
t.pencolor('white')
t.speed(0)
c = 0
d = 0
while True:
    for i in range(18):#z
        t.color(A[i%2])#num of color
        t.forward(40)
        t.right(20)#360/z
    t.right(30)#x
    c+= 1
    if c>=360/30:#360/x
        t.right(60) #y
        t.forward(25)
        c = 0
        d+=1
        if d>=6:#360/y
            break
turtle.done()