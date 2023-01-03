from cgitb import reset
from zad6ktesty import runtests 

def haslo ( S ):
    result = [0 for _ in range(len(S))]
    result[0] = 1
    result[1] = 1

    if int(S[0:2]) <= 26 and int(S[0:2]) != 10:
        result[1] = 2
    
    for i in range(2, len(S)-1):
        if S[i+1] == '0' or S[i] == '0' or S[i-1] == '0':
            if S[i-1] == '0' and S[i] == '0' or  S[i+1] == '0' and S[i] == '0':
                return 0
            if S[i] == '0' and int(S[i-1]) > 2:
                return 0
            result[i] = result[i-1]
        elif int(S[i-1:i+1]) <= 26:
            result[i] = result[i-1] + result[i-2]
        else:
            result[i] = result[i-1]
    
    if int(S[-2:]) <=26:
        result[-1] = result[-2] + result[-3]
    else:
        result[-1] = result[-2]

    print(result)
    return result[-1]
    

runtests ( haslo )