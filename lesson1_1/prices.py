display_price = int (15000)
system_unit_price = int (40000)
input_device_price = int (7300)
n = int (input ('Сколько компьютеров вам нужно? '))
price = (display_price + system_unit_price + input_device_price) * n
print ('Цена всех компьютеров: ' + str (price))