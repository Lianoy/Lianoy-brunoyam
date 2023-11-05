import random

def bubble_sort(lst):
    lst_size = len(lst)
    for i in range (0, lst_size-1):
        for j in range(1,lst_size-i):
            if lst[j] < lst[j-1]:
                lst[j], lst[j-1] = lst[j-1], lst[j]
        print (lst)
    return lst

# lst = [int(x) for x in input().split()]
n=10
i=0
lst=[]
for i in range(n):
    lst.append(random.randint(0, 100))
bubble_sort(lst)
print(lst)