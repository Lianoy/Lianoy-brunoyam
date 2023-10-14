## Task #1
import math
def area (a,b,c):
    p = (a + b + c) / 2
    s = math.sqrt(p*(p-a)*(p-b)*(p-c))
    return s

a = float (input ("Ввведите первую сторону:"))
b = float (input ("Ввведите вторую сторону:"))
c = float (input ("Ввведите третью сторону:"))
print ('Площадь треугольника равна', area(a,b,c))

## Task #2
s = '''Было просто пасмурно, дуло с севера
А к обеду насчитал сто градаций серого
Так всегда первого ноль девятого
То ли весь мир сошёл с ума, то ли я - того
На столе записка от неё смятая
Недопитый виски допиваю с матами
Посмотрю в окно, допишу главу
Первое сентября, дворник жжёт листву
Серым облакам наплевать на нас
Если знаешь как жить - живи
Ты хотела плыть как все - так плыви'''
m = s.split()
short_words = ''
for i in m:
    if len(i) < 5:
        short_words += i + ' '
print (short_words)

## Task #3
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
