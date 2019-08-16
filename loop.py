for i in range(10):
    print("I want to be a great programmer")
print("-------------------------------------------")
for i in range(5):
    print(i)
print("-------------------------------------------")

import turtle

turtle.shape("turtle")
turtle.speed(1)
for i in range(4):
    turtle.forward(100)
    turtle.left(90)
turtle.exitonclick()
print("Square Box showed")
print("------------------------------------------")
print("Sum of 50 of 1")
result = 0
for i in range(50):
    result = result+1

print(result)
print('-----------------------------------------')
print('Sum of !+2+3+------')
result=0
num=1
for i in range(50):
    result=result+num
    num=num+1
print(result)
print("-----------------------------------------")
print("Diffrerent Way to find sum of 1+2+3+------------")
result=0
for num in range(51):
    result+=num
print(result)
print("-----------------------------------------")
print("range function with two peramitter")
result=0
for num in range(1,51):
    result+=num
print(result)
print("----------------------------------")
print("Increase loop with 5 gap")
for i in range(1,50,5):
    print(i)
print("----------------------------------")
print("1 to 100 thats divided by 5 and also sum of div")
result=0
for num in range(101):
    if num%5==0:
        result+=num
        print(num)
print(result)
print("----------------------------------------------")
print("1 to 100 thats increses by 5 and also sum of number")
result=0
for num in range(5,101,5):
    result+=num
    print(num)
print(result)
print("---------------------------------------------")
