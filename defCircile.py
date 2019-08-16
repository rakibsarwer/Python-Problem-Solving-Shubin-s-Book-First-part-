import turtle

def squareBox(side_len):
    for i in range(4):
        turtle.forward(side_len)
        turtle.left(90)

counter=0
turtle.speed(9)
turtle.shape('turtle')
turtle.color('orange')
while counter < 90:
    squareBox(100)
    turtle.right(4)
    counter += 1
turtle.exitonclick()
