def myFnc(k=9):
    print("Value :",k)

myFnc(10)
myFnc()

print("---------------------------")
print("Multiple Default peram ")

def multPeramFnc(x,z,y=10):
    print("X :",x)
    print("y :",y)
    print("z :",z)

multPeramFnc(4,29,17)

print("---------------------")
print("Multiple default perameter solved problem of value assiagning")

def myMultFnc(x,z,y=7):
    print("X :",x," y :",y," z :",z)
    

myMultFnc(x=1,y=10,z=20)
a=5
b=8
myMultFnc(x=a,z=b)
a=20
b=30
c=40
myMultFnc(z=b,x=c,y=a)