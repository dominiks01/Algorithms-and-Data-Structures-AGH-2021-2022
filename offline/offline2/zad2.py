from zad2testy import runtests

def quick_sort(A, p, r):
    s = []
    s.append((p, r))
    while len(s) > 0:
        i, j = s.pop()
        if j > i:
            q = partition(A, i, j)
            if q - i < j - q:
                s.append((i, q-1))
                s.append((q+1, j))
            else:
                s.append((q+1, j))
                s.append((i, q-1))


def partition(A, p, r):
    x = A[r][0]
    i = p - 1

    for j in range(p, r):
        if A[j][0] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    
    A[i+1], A[r] = A[r], A[i+1]

    return i + 1


def depth(L):
    result = 0 
    quick_sort(L, 0, len(L) - 1)
    i = 0

    L2 = []

    while i < len(L):
        j = i + 1
        act = 0
        max_value = L[i][1]
        while j < len(L) and L[i][0] == L[j][0]:
            max_value = max(max_value, L[j][1])
            j += 1
            act += 1
        L2.append((L[i][0], max_value, act))
        i = j 

    print(L2)


    while i < len(L):
        act = 0
        j = i 

        while j = i + 1
    

    

    return result
    

runtests( depth ) 
