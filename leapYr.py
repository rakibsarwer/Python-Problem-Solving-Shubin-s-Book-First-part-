year = input("Enter the year :")
year = int(year)

if year % 4 == 0:
    print(year, " is Leap Year")
else:
    if year %100 == 0:
        if year%400==0:
            print(year, "is Leap Year")
        else:
            print(year," is not Leap year")

    else:
        print(year, " is not Leap year")


print("Program Terminated")

if year % 100 !=0 and year % 4==0:
    print(year, "is leap year")
elif year % 100==0 and year == 400:
    print(year, " is Leap year")
else:
    print(year, " is nor Leap Year")