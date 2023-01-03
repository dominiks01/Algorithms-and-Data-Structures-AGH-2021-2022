import re
from zad1ktesty import runtests

def roznica( S ):
    #Tutaj proszę wpisać własną implementację
    result = [0]*len(S)

    if S[0] == '0':
        result[0] = 1
    
    for i in range(1, len(S)):
        if S[i] == '1':
            result[i] = max(0, (result[i-1]-1))
        else:
            result[i] = max(1, (result[i-1]+1))

    if max(result) == 0:
        return -1
    return max(result)

runtests ( roznica )