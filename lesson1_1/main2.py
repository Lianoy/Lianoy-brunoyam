import random
import math
minN = int (input ('Введите минимальное число диапазона:'))
maxN = int (input ('Введите максимальное число диапазона:'))
n = random.randint (minN, maxN)
p = math.ceil(math.log2(maxN-minN))
x = 0
print ('Попробуйте угадать! Количество попыток: ' + str(p))
while x <= p:
    x += 1
    d = int (input ('Попытка №' + str(x) + ':'))
    if d == n:
        print ('Вы угадали!')
        break
    elif d < n:
        print ('Не угадали! Число больше!')
    else:
        print ('Не угадали! Число меньше!')
print ('Вы использовали ' + str(x) + ' попыток. Загаданное число: ' + str(n))