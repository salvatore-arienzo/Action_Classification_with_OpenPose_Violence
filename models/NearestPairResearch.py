import math


def coppiaPiuVicina(pX, pY, n):
    sX = []
    dX = []
    sY = []
    dY = []
    pq = ()
    if n <= 3:
        return ricercaEusastiva(pX, n)
    else:
        p = pX[math.trunc(n / 2)]
        j = 0
        k = 0
        for i in range(0, math.trunc(n / 2)):
            sX.append(pX[i])
        for i in range(math.trunc(n / 2), n):
            dX.append(pX[i])
        for i in range(0, n):
            if pY[i][0] < p[0]:
                sY.append(pY[i])
            elif (pY[i][0] == p[0]) and (pY[i][1] < p[1]):
                sY.append(pY[i])
            else:
                dY.append(pY[i])

        pqS = coppiaPiuVicina(sX, sY, math.trunc(n / 2))

        pS = pqS[0]
        qS = pqS[1]
        pqD = coppiaPiuVicina(dX, dY, math.trunc((n + 1) / 2))
        pD = pqD[0]
        qD = pqD[1]
        if dist(pS, qS) < dist(pD, qD):
            d = dist(pS, qS)
            pq = (pS, qS)
        else:
            d = dist(pD, qD)
            pq = (pD, qD)
        Pd = []
        for i in range(0, n):
            if abs(pY[i][0] - p[0]) <= d:
                Pd.append(pY[i])
        for i in range(0, len(Pd)):
            for j in range(i + 1, minimo(i + 11, len(Pd))):
                if dist(Pd[i], Pd[j]) < d:
                    d = dist(Pd[i], Pd[j])
                    pq = (Pd[i], Pd[j])
        return pq


def ricercaEusastiva(punti, n):
    if n >= 2:
        pq = (punti[0], punti[1])
        if n == 2:
            return pq
        min = dist(punti[0], punti[1])
        if dist(punti[1], punti[2]) < min:
            min = dist(punti[1], punti[2])
            pq = (punti[1], punti[2])
        if dist(punti[0], punti[2]) < min:
            pq = (punti[0], punti[2])
        return pq


def dist(p, q):
    x1 = p[0]
    y1 = p[1]
    x2 = q[0]
    y2 = q[1]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def minimo(a, b):
    if a <= b:
        return a
    return b


def ordinamento(array, tipo):
    coordinata = abs(tipo - 1)
    for i in range(len(array)):
        least = i
        for k in range(i + 1, len(array)):
            if array[k][tipo] < array[least][tipo]:
                least = k
            elif (array[k][tipo] == array[least][tipo]) and (array[k][coordinata] < array[least][coordinata]):
                least = k
        swap(array, least, i)


def swap(A, x, y):
    temp = A[x]
    A[x] = A[y]
    A[y] = temp


def inserimentoOrdinato(array, val, tipo):
    coordinata = abs(tipo - 1)
    #print(array)
    if len(array) == 0:
        array.append(val)
        return array
    for i in range(len(array)):
        if val[tipo] < array[i][tipo]:
            array.insert(i, val)
            return array
        elif (array[i][tipo] == val[tipo]) and (val[coordinata] <= array[i][coordinata]):
            array.insert(i, val)
            return array
    array.append(val)
    return array


'''
x = [(2, 5), (2, 11), (3, 2), (3, 9), (4, 6), (5, 12), (7, 8), (8, 3), (9, 11), (10, 2),
     (10, 15), (11, 6), (12, 6), (12, 14), (13, 9), (14, 7), (16, 5), (17, 8), (18, 1), (18, 4)]
y = [(18, 1), (3, 2), (10, 2), (8, 3), (18, 4), (2, 5), (16, 5), (4, 6), (11, 6), (12, 6),
     (14, 7), (7, 8), (17, 8), (3, 9), (13, 9), (2, 11), (9, 11), (5, 12), (12, 14), (10, 15)]
'''
x = [(14, 7), (16, 5), (17, 8),  (18, 4), (18, 1), (2, 5), (2, 11), (10, 15), (11, 6), (12, 6), (12, 14), (13, 9),
     (3, 2), (3, 9), (4, 6), (5, 12), (7, 8), (8, 3), (9, 11), (10, 2)]

y = [(14, 7), (16, 5), (17, 8), (18, 1), (18, 4), (2, 5), (2, 11), (10, 15), (11, 6), (12, 6), (12, 14), (13, 9),
     (3, 2), (3, 9), (4, 6), (5, 12), (7, 8), (8, 3), (9, 11), (10, 2)]
'''
ordinato = []
for i in range(len(x)):
    inserimentoOrdinato(ordinato, x[i], 1)

'''
ordinamento(x, 0)
ordinamento(y, 1)

#print(y)
#print(x)
#print(coppiaPiuVicina(x, y, len(x)))

