# Zadanie offline nr. 1 

# insertion sort z warunkiem k-chaotycznosci
# sprawdzamy jedynie k-wartości od miejsca początkowego 
# dla k == n zakładamy złożoność pesymistyczną równą zwykłemu insertion sort, stąd O(n^2)

# złożoność algorytmu O(n^2)

from zad1testy import runtests

# funkcja pomocnicza 
#def print_list(p):
#    while p is not None:
#        print(p.val, end=" ", sep="")
#        p = p.next


def insertion_sort(array , k : int):
    for i in range(1, len(array)):
        key = array[i]

        j = i - 1
        while j >= 0 and key < array[j] and i - j <= k:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key
    
    return array


def sort_h(p, k):
    return insertion_sort(p, k)
        

runtests(sort_h)