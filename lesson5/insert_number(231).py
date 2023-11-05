import random

def vstavka(lst,number,index):
    lst.append(number)
    i = len(lst)-1
    while i > index:
        lst[i], lst [i-1] = lst [i-1], lst [i]
        i-=1
        # print("process", lst)

n=10
lst=[]
for i in range(n):
    lst.append(random.randint(-1000, 1000))
lst.sort()
print(lst)
inpt = list(map(int,input("Введите число и место: ").split()))
vstavka(lst,inpt[0],inpt[1])
print(lst)