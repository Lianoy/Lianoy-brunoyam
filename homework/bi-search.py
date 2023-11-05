import random

arrN=[]
arrK=[]
res=[]
n=5
k=5
i=0
j=0
while i < n:
    arrN.append(random.randint(0,100))
    i += 1
while j < k:
    arrK.append(random.randint(0,100))
    j += 1
arrN.sort()
print(arrN)
print(arrK)

def three_max(k,*a):
    answ = a[0]
    length = 1000
    for j in a:
        if abs(k-j) < length:
            answ = j
            length = abs(k-j)
    return answ

for k_ele in arrK:
    left=0
    right=n-1
    while (right-left) > 1:
        r = (right - left) // 2
        if k_ele < arrN[r]:
            right = right - r -1
        elif k_ele > arrN[r]:
            left += r + 1
        else:
            break
    r = left
    if r == 0:
        res.append(three_max(k_ele,arrN[r],arrN[r+1]))
    elif r == n:
        res.append(three_max(k_ele,arrN[r-1],arrN[r]))
    else:
        res.append(three_max(k_ele,arrN[r-1],arrN[r],arrN[r+1]))
print(arrN)
print(arrK)
print(res)