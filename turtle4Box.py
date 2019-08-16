import turtle
turtle.shape("turtle")
turtle.speed(2)
turtle.penup()
turtle.backward(300)
for i in range(0,4):
    
    turtle.penup()
    turtle.forward(110)
    for i in range(4):
        turtle.pendown()
        turtle.forward(100)
        turtle.left(90)
turtle.exitonclick()