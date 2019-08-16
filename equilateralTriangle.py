import turtle
turtle.speed(2)
turtle.color('red')

def equalTri(side_len):
    turtle.forward(side_len)
    turtle.left(120)
    turtle.forward(side_len)
    turtle.left(120)
    turtle.forward(side_len)

equalTri(100)
turtle.exitonclick()