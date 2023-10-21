def count_days (sec):
    min = sec // 60
    hours = min // 60
    days = hours // 24
    sec = sec % 60
    min = min - hours * 60
    hours = hours - days * 24
    print (f"Это будет {days} дней {hours} часов {min} минут {sec} секунд")

x = int (input ("Введите секунды:"))
count_days (x)

########################################################

import re

str = input ("Введите числа через запятую:")
list_num = re.split (",", str)
negative = []
positive = []
for i in list_num:
    if int(i) < 0:
        negative.append (int(i))
    else:
        positive.append (int(i))
print (positive)
print (negative)

########################################################

def print_even(num):
    if (num % 2) == 0:
        print (num)

numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217]
for i in numbers:
    if i == 237:
        break
    else:
        print_even (i)
