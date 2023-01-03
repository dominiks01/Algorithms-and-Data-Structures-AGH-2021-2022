from zad5ktesty import runtests
    

def garek ( A ):
    result = [[0 for _ in range(len(A))] for _ in range(len(A))]

    for i in range(1, len(A)):
        result[i-1][i] = max(A[i-1], A[i])
    
    for i in range(3, len(A), 2):
        for j in range(len(A)-i):
            a1 = min(result[j][i+j-2], result[j+1][i+j-1])
            a2 = min(result[j+1][i+j-1], result[j+2][i+j])
            result[j][i+j] = max(a1+A[j+i], a2+A[j])

    return result[0][len(A)-1]

runtests ( garek )