import turtle

turtle.color("green")
turtle.speed(1)

height = 5
width = 5
count = 5
turtle.penup()
for x in range(height):
    
    for y in range(width):
        
        if x==0:
            turtle.dot()
        turtle.forward(20)
    turtle.dot()    
    turtle.backward(20*width)
    turtle.right(90)
    turtle.forward(20)
    turtle.left(90)
    width-=1
turtle.exitonclick()
    