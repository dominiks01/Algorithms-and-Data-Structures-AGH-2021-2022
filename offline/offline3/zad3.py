# Bucket-Sort z zaimplementowanym quick-sortem i insertion_sortem 
# Index elementu wyznaczany jest ze wzoru (X - min)*Ilość bucketów / (różnica wartości elementu największego i najmniejszego)
# Rozwiązanie nie używa prawdopodobieństwa 

# Złożoność czasowa O(n^2)

from zad3testy import runtests

def insertion_sort(arr):
    for i in range(len(arr)-1):
        ind_max = i
        for j in range(i, len(arr)):
            if arr[ind_max] > arr[j]:
                ind_max = j 
        arr[ind_max], arr[i] = arr[i], arr[ind_max]
   

def bucket_sort(P, T):
    maxElement  = max(P)
    minElement = min(P)
    n = len(P)//10
    result = [[] for _ in range(n+1)]

    for i in range(len(P)):
        index = (P[i] - minElement) / (maxElement - minElement) * n
        result[int(index)].append(P[i])

    p_result = []
    for i in result:
        if i is not None:
            if len(i) >= 10:
                quick_sort(i, 0, len(i)-1)
            else:
                insertion_sort(i)
            p_result.extend(i)

    return p_result 


def partition(A, p, r):
    x = A[r]
    i = p-1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1


def quick_sort(A, p, r):
    while p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q - 1)
        p = q + 1


def SortTab(T,P):
    return bucket_sort(T, P)


runtests( SortTab )