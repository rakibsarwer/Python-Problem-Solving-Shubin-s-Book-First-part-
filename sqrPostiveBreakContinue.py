while True:
    n = input("Enter The Positive number to run || 0 for exit :")

    n=int(n)

    if n<0:
        print("Only Positive number is allowed ")
        continue
    if n==0:
        break
    print("Square of ",n," = ",n*n)