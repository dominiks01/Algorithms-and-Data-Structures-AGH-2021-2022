from unittest import result
from zad4ktesty import runtests

def falisz ( T ):
    result = [[0 for _ in range(len(T))] for _ in range(len(T))]

    for i in range(1, len(T)):
        result[0][i] += (result[0][i-1] + T[0][i])

    for i in range(1, len(T)):
        result[i][0] += (result[i-1][0] + T[i][0])

    for i in range(1, len(T)):
        for j in range(1, len(T)):
            result[i][j] = (min(result[i-1][j], result[i][j-1]) + T[i][j])
    
    return result[len(T)-1][len(T)-1]

runtests ( falisz )
