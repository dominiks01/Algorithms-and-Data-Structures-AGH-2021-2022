from zad9ktesty import runtests
from math import inf

def _prom(P, result, g, d, i):
    if i == len(P):
        return 0

    if result[i][d][g] != -1:
        return result[i][d][g]
    
    if P[i] > g and P[i] > d:
        result[i][d][g] = 0
        return 0
    
    if P[i] > g:
        result[i][d][g] = _prom(P, result, g, d-P[i], i+1) + 1
        return result[i][d][g]
    
    elif P[i] > d:
        result[i][d][g] = _prom(P, result, g-P[i], d, i+1) + 1
        return result[i][d][g]
    
    else:
        w1 = _prom(P, result, g, d-P[i], i+1)
        w2 = _prom(P, result, g-P[i], d, i+1)
        result[i][d][g] = max(w1, w2) +1
    return result[i][d][g]
    
     

def prom(P, g, d):
    result = [[[-1 for _ in range(g+1)] for _ in range(d+1)] for _ in range(len(P))]
    _prom(P, result, g, d, 0)

    


runtests ( prom )