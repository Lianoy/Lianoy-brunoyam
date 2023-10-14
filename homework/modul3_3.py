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
def maximum (list):
    max2 = ''
    for i in list:
        
        
    
from random import randint
m = [randint(0,100) for i in range(7)]
print (m)
max1 = ''
# for i in m:
#     max1 += comparision
i = 0
for val1 in m:
    for val2 in m[i:len(m)]:
        if val1 > val2:
            max1 += str(val1)
    i += 1
print (max1)
