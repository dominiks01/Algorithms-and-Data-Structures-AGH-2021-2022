import re
from zad8ktesty import runtests 

def napraw ( s, t ):
    result = [[0 for _ in range(len(s))] for _ in range(len(t))]

    for i in range(len(s)):
        if t[0] == s[i] and result[0][i-1] == i:
            result[0][i] = result[0][i-1]
        else:
            result[0][i] = result[0][i-1] + 1

    for i in range(len(t)):
        if s[0] == t[i] and result[i-1][0] == i:
            result[i][0] = result[i-1][0]
        else:
            result[i][0] = result[i-1][0] + 1

    
    for i in range(1, len(t)):
        for j in range(1, len(s)):
            if t[i] == s[j]:
                result[i][j] = result[i-1][j-1]
            else:
                result[i][j] = min(result[i-1][j], result[i][j-1], result[i-1][j-1]) + 1
    
    return result[len(t)-1][len(s)-1]

runtests ( napraw )