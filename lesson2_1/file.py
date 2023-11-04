# message='Hello World'
# f=open('text.txt','w') #для дозаписи нужен режим a+
# f.write(message)
# f.close()

# with open('text.txt','w') as f:
#     message=f.read()
#     print(message)
    #f.write(message)

# arr=[]
# with open('text.txt','r') as f:
#     for i in f:
#         arr.append(int(i))
# print(arr)

# import json
# with open('values.json','r') as f:
#     result=json.load(f)
#     print(result['Las'])

import random

def filling(name,fill):
    with open(name,'w') as f:
        for j in range(len(fill)):
            f.write(str(arr[j]) + '\t')

arr=[]
for i in range(20):
    arr.append(random.randint(0, 100))

filling('text.txt',arr)
