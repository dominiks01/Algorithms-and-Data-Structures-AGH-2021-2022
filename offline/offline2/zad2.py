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
    new_array = []

    for x,y in L:
        new_array.append((x,1))
        new_array.append((y,-1))
    
    quick_sort(new_array, 0, len(new_array)-1)

    result = 0
    actual_value = 0
    
    for i in range(0, len(new_array)-1):
        actual_value += new_array[i][1] 
        result = max(result, actual_value)

    return result
    

runtests( depth ) 
