import turtle
sc = turtle.Screen()
sc.bgcolor("darkblue")
tess = turtle.Turtle()
tess.shape("turtle")
tess.color("yellow")
tess.up()

distance = 5

for _ in range(50):
    tess.stamp()
    tess.forward(distance)
    tess.right(24)
    distance+=3
sc.exitonclick()
    
    