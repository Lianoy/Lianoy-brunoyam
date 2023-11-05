import random

def bubble_sort(lst):
    k=0
    lst_size = len(lst)
    for i in range (0, lst_size-1):
        for j in range(1,lst_size-i):
            if lst[j] < lst[j-1]:
                lst[j], lst[j-1] = lst[j-1], lst[j]
                k+=1
        # print (lst)
    print(lst)
    return k

# lst = [int(x) for x in input().split()]
n=10
lst=[]
for i in range(n):
    lst.append(random.randint(-1000, 1000))
print(lst)
print(bubble_sort(lst))