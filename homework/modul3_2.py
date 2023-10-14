##Task #1
l = [1, 4, 1, 6, "hello", "a", 5, "hello"]
a = []
length = len(l)+1
for i, val in enumerate(l):
    for j in l[i+1:length]:
        if val == j:
            a.append(val)
print (a)

## Task #2
from random import randint
n = 5
m = [[randint(0,100) for i in range(n)] for j in range(n)]
max1 = m[0][0]
for i in range(n):
    print (m[i])

for i in range(n):
    for j in m[i]:
        if max1 < j:
            max1 = j
print (max1)

## Task #3
d = {'name1': 'id1', 'name2': 'id2', 'name3': 'id3'}
d1 = {}
for name, id in d.items():
    d1[id] = name
print (d1)
