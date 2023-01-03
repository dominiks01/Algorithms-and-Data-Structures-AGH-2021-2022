# Algorytmu nie działa poprawnie

# Jeśli graf jest spójny - usuwam najmniejszą krawędź aż przestanie być spójny
# Jeśli nie jest spójny - dodaję kolejną z kolei krawędź 
# Badam tak wszystkie możliwe kombinacje spójnych grafów wsród których powinnien znajdować się nasz podgraf o najmniejszej różnicy

from math import sqrt
from zad8testy import runtests
from math import inf
from math import ceil


def getLen(x, y):
    return ceil(sqrt((y[0] - x[0])**2 + (y[1] - x[1])**2))


def check_connection(A, n, p, r):
    # test spójności - nie działa i działać nie może

    if r - p + 1 < n-1:
        return False

    q = (r-p+1)
    V = [q for i in range(n)]

    for i in range(r-p+1):
        a = A[p+i]
        if V[a[1]] == q and V[a[0]] == q:
            V[a[1]] = V[a[0]] = i
        elif V[a[0]] < V[a[1]]:
            V[a[1]] = V[a[0]]
        else:
            V[a[0]] = V[a[1]] 
        
    return not q in V 


def highway(A):
    n = len(A)
    T = []
    for i in range(n):
        for j in range(n-i-1):
            T.append((i, j+i+1, getLen(A[i], A[j+i+1])))
    
    T.sort(key= lambda x: x[2])

    diff = inf

    p, r = 0, 0

    while r != len(T) - 1:
        if check_connection(T, n, p, r):
            x1 = max(T[p:r+1], key=lambda x: x[2])[2]
            x2 = min(T[p:r+1], key=lambda x: x[2])[2]
            diff = min(diff, x1-x2)
            p += 1
        else: 
            r += 1
    
    while check_connection(T, n, p, r) and r - p >= n - 1:
            x1 = max(T[p:], key=lambda x: x[2])[2]
            x2 = min(T[p:], key=lambda x: x[2])[2]

            if x2 - x1 < diff:
                diff = x2 - x1 
            
            p += 1

    return diff

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( highway, all_tests = True)