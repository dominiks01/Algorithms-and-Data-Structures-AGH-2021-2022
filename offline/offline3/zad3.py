# Bucket-Sort z zaimplementowanym quick-sortem 

# Alogytm do poprawy, nie korzysta z opisu przedziałów 

from zad3testy import runtests
from random import randint


def insertion_sort(arr):
    for i in range(len(arr)-1):
        ind_max = i
        for j in range(i, len(arr)):
            if arr[ind_max] > arr[j]:
                ind_max = j 
        arr[ind_max], arr[i] = arr[i], arr[ind_max]
   

def bucket_sort(P, T):
    result = [[] for _ in range(len(P))]

    for i in range(len(P)):
        result[int(P[i])].append(P[i])
    
    for i in result:
        if i is not None:
            quick_sort(i, 0, len(i)-1)
    
    p_result = []

    for i in result:
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