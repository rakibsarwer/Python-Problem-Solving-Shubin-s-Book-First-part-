def summ(a,b):
    return a+b
def subs(a,b):
    return a-b
def mult(a,b):
    return a*b
def div(a,b):
    return a/b
def sqr(a,b):
    return a**b
def mod(a,b):
    return a%b
def divint(a,b):
    return a//b


inp1=input("Enter First Number :")
inp2=input("Enter second Number :")
inp3=input("Enter Method name : (exmple: sum,sub, div, mult, sqr ,mod,divint Only one method)")

num1 = int(inp1)
num2 = int(inp2)
if inp3=='sum':
    print(summ(num1,num2))
elif inp3=='sub':
    print(subs(num1,num2))
elif inp3=='div':
    print(div(num1,num2))
elif inp3=='mult':
    print(mult(num1,num2))
elif inp3=='sqr':
    print(sqr(num1,num2))
elif inp3=='mod':
    print(mod(num1,num2))
elif inp3=='divint':
    print(divint(num1,num2))