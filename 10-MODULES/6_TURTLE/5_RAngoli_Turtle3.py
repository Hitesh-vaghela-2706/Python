import turtle
t = turtle.Turtle()
col = ('yellow','green','white','pink','orange','cyan')
screen = turtle.Screen()
screen.bgcolor('blue')
t.speed(0)
for i in range(100):
	t.color(col[i%6])
	t.forward(i*2)
	t.left(59)
	t.width(3)
turtle.done()
