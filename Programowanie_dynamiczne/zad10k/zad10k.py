from collections import deque
from zad10ktesty import runtests
from math import sqrt
import sys
from math import floor

sys.setrecursionlimit(10000)

# funkcja rekurencyjna
def findMinCoins(S, target):
    T = [0] * (target + 1)

    for i in range(1, target + 1):
        T[i] = sys.maxsize

        for c in range(len(S)):
            if i - S[c] >= 0:

                result = T[i - S[c]]
                if result != sys.maxsize:
                    T[i] = min(T[i], result + 1)
 
    return T[target]


def dywany ( N ):
    result = [i**2 for i in range(1, floor(sqrt(N))+1)]
    n = findMinCoins(result, N)

    q = []

    while N:
        for j in result:
            if findMinCoins(result, N-j) == n - 1:
                q.append(sqrt(j))
                n = n-1
                N = N-j
                break

    return q


runtests( dywany )

