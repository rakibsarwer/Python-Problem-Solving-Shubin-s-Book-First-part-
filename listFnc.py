def add_num(numbers):
    result=0
    for number in numbers:
        print(number)
        result+=number
    return result

result = add_num([2,4,6,8])
print(result)


print("-------------------")
print("Assigning new value in list")

def testList(li):
    li[0]=10
my_li=[2,3,4,5,2,8]
print("Befor calling function",my_li)
testList(my_li)
print("After calling function",my_li)
new_li = my_li

print("-------")
new_li[0]=180
print(new_li)
print(my_li)

print("----------------------")
print("Using built in sum function")
list_new = [2,3,4,5,6,1]
print(len(list_new))
res= sum(list_new)
print(res)

print("-----------------------")
print("Find avarage of list value")
list_my = [2,3,4,5,6,7,8,9,1]
len_list = len(list_my)
sum_list = sum(list_my)
avarge = sum_list/len_list
print(avarge)

print("-------------------")
print("Find Multiplication Table")

def multTbl(num):
    counter = 0
    while counter <=10:
        print(num," X ",counter," = ", num*counter)
        counter+=1


inp= input("Enter The Number For Multiplication table :\n")
inp = int(inp)
multTbl(inp)