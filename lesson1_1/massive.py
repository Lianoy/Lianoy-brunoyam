import array
import random
arr=array.array('i',[])
for i in range(20):
    arr.append(random.randint(0, 100))
#arr = array.array('i',[5,7,2,9,1,48,45,65,223,12,87,54])
arr2 = array.array('i')
x=0
y=0
##len(arr) - длина массива
for i in arr:
    if not i%2:
        if y%2:
            arr2.append(y)
    y += 1
print(arr)
print (arr2)