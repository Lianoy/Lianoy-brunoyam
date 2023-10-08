import math

def get_path(P,u,v):
    path = [u]
    while u != v:
        u = P[u][v]
        path.append(u)
    return path

metro = ['Проспект Ветеранов','Ленинский проспект','Автово','Кировский завод']
V=[]
i = 0
while i < 73:
    L=[]
    j = 0
    while j < 73:
        if i == j:
            L.append(0)
        elif (i - j) == 1:
            if j != 19 and j != 37 and j != 49 and j != 57:
                L.append(1)
        elif (i - j) == -1:
            if j != 20 and j != 38 and j != 50 and j != 58:
                L.append(1)
        elif (j == 29 and i == 45) or (i == 29 and j == 45): #Гостинка
            L.append(0.1)
        elif (i == 7 and j == 27) or (j == 7 and i == 27): #Техноложка
            L.append(0.1)
        elif (i == 8 and j == 65) or (i == 65 and j == 8): #Пушкинская
            L.append(0.1)
        elif (i == 9 and j == 56) or (i == 56 and j == 9): #Владимирская
            L.append(0.1)
        elif (i == 10 and j == 44) or (i == 44 and j == 10): #Восстания
            L.append(0.1)
        elif (i == 43 and j == 54) or (i == 54 and j == 43): #Ал.Невск.
            L.append(0.1)
        elif (i == 28 and j == 57) or (i == 28 and j == 66) or (i == 57 and j == 66) or (i == 57 and j == 28) or (i == 66 and j == 28) or  (i == 66 and j == 57): #Тройка
            L.append(0.1)
        else:
            L.append(math.inf)
        j += 1
    #print (L)
    V.append(L)
    i += 1

#print(V)

N = 72 ##число вершин графа
P = [[v for v in range(N)] for u in range(N)] ##начальный список предыдущих вершин для поиска кратчайших маршрутов

for k in range(N):
    for x in range(N):
        for y in range(N):
            d = V[x][k] + V[k][y]
            if V[x][y] > d:
                V[x][y] = d
                P[x][y] = k ##номер промежуточной вершины при движении от i до j

#print(V)
#нумерация вершин с 0
start = 1
end = 45
print(get_path(P,start,end))
