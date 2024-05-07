from turtle import *
speed(0)
hideturtle()
c = ("cyan","blue","red")
pensize(3)
bgcolor("black")

for i in range(350) :
    pencolor(c[i%3])
    fd(i)
    lt(100*2)
    lt(5*2)
done()