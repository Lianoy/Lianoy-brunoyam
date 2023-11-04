def comparision (a, b): ## найти "большее" число
    if a == b:
        return a
    if int(str(a)[0]) > int(str(b)[0]):
        return a
    elif int(str(a)[0]) < int(str(b)[0]):
        return b
    else: ##первая цифра в числах одинаковая
        if a < 10 or b <10:
            if a > b:
                return b
            else:
                return a
        else:
            if int(str(a)[1]) > int(str(b)[1]):
                return a
            else:
                return b

def maximum (list):
    x = list[0]
    for k in list:
        x = comparision (x, k)           
    return x      
    
from random import randint
n=7
m = [randint(0,99) for i in range(n)]
print (m)
max1 = ''
left = []
for i in m:
    left.append(i)

for i in range(n):
     max2 = maximum (left) ##ищем наибольшее из оставшихся чисел
     max1 += str (max2)
     left.remove (max2)
print (max1)