import random
# import math
arrN=[]
arrK=[]
# res=[]
n=5
k=5
r=0
# arrN=[1,3,5,7,9]
for i in range(n):
    arrN.append(random.randint(0, 100))
for i in range(k):
    arrK.append(random.randint(0, 100))
arrN.sort()
print(arrN)
print(arrK)

while i<=k:
    r = int(abs(arrN[0]-arrN[0]))
    res[i].append(arrN[0])
    res[i].append(r)
    i+=1
print (res)


for i in arrK:    
    for j in arrN:
        r = abs(arrK[i]-arrN[j])
        if r <= res[i][1]:
            if arrN[j] < res[i][0]:
                res[i][0] = arrN[j]
                res[i][1] = r

print (res)