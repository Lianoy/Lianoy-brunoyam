import random

def insert_sort(lst):
    lst_size = len(lst)
    for i in range(1,lst_size):
        while i > 0 and lst[i] < lst [i-1]:
            lst[i], lst [i-1] = lst [i-1], lst [i]
            i-=1
        print("process", lst)


# lst = list(map(int,input().split()))
n=10
lst=[]
for i in range(n):
    lst.append(random.randint(0, 100))
insert_sort(lst)
print("result", lst)