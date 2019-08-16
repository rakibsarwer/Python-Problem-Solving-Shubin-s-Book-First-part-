program_terminate = False

while not program_terminate:
    n1=input("Enter num1 value :\n")
    n2=input("Enter num2 value :\n")
    n1=int(n1)
    n2=int(n2)
    con = input("Enter The method like 'quit,sub,add' only one from here :\n")
    while True:
        if con=="quit":
            program_terminate=True
            break
        if con not in ["add","sub"]:
            print("Unknown Method")
            break
        if con=="add":
            print("sum is = ",n1+n2)
            break
        if con =="sub":
            print("num2-num1 number\'s sub is = ",n2-n1)
            break