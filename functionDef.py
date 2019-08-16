def add_number(n1,n2):
    return n1+n2

try:
    n1=input("Enter Int First number :")
    n2 = input("Enter Int Second Number :")

    n1 = int(n1)
    n2 = int(n2)
    sum=add_number(n1,n2)
    print(sum)
except:
    print("Enter only Integer Numbers")
finally:
    file=open('db.txt','w')
    file.write("sum is :"+str(sum))
    file.close()
    print("New File Created with value")