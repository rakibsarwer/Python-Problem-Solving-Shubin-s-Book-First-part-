def myfnc(y):
    print("Local variable y : ",y)
    print("Global Variable x : ", x)


x=20
myfnc(x)


try:
    print(y)
except:
    print("Some Error")
finally:
    print("Program Executed")
