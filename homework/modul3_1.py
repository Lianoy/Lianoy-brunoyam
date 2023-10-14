##Task 1
x = int (input ('Текущий размер вклада:'))
y = int (input ('Цель:'))
p = int (input ('Проценты по вкладу:'))

n = 1
while x < y:
    x = float (int((x + x*p/100)*100))/100
    n += 1
print ('Цель будет достигнута через', n, 'лет')

##Task 2
n = int (input ('Количество строк:'))
a = 0
while a <= n:
    print ('for - частный случай while')
    a += 1

##Task 3
s = str (abs (int (input ('Введите число:'))))
sum = 0
for i in range(len(s)):
    sum += int(s[i])
print ('Сумма всех цифр этого числа -', sum)
