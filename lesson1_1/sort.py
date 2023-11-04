numbers = [34,0,-56,7,3,8,9,-3,-456,67,234,0,78,-34]
negative=[]
positive=[]
null=[]

for n in numbers:
    if n < 0:
        negative.append(n)
    elif n == 0:
        null.append(n)
    else:
        positive.append(n)
print (negative)
print (positive)
print (null)