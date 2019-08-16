import turtle

turtle.speed(1)
turtle.color("red")

height = 5
width = 5
turtle.penup()
for i in range(height):
    for j in range(width):
        turtle.dot()
        turtle.forward(20)
    turtle.backward(20*width)
    turtle.right(90)
    turtle.forward(20)
    turtle.left(90)
turtle.exitonclick()