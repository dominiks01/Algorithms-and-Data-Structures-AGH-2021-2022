from kol1atesty import runtests

def SieveOfEratosthenes():
    prime = [True for i in range(201)]
    p = 2
    while (p * p <= 200):
        if (prime[p] == True):
             for i in range(p * p, 201, p):
                prime[i] = False
        p += 1
 
    prime_array = []

    for p in range(2, 201):
        if prime[p]:
            prime_array.append(p)
    
    return prime_array


global prime_value_array
prime_value_array = SieveOfEratosthenes()


def get_string_value(string_to_int):

    result = 1
    global prime_value_array

    for i in string_to_int:
        result *= prime_value_array[ord(i) - ord('a')]
    
    return result


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


def g(T):
    test_array = [get_string_value(i) for i in T]
    quick_sort(test_array, 0, len(test_array)-1)

    act = 1
    max_value = 0

    for i in range(1, len(test_array)):
        if test_array[i] == test_array[i-1]:
            act += 1
        else:
            max_value = max(max_value, act)
            act = 1
    
    return max_value


# Zamien all_tests=False na all_tests=True zeby uruchomic wszystkie testy
runtests( g, all_tests=True )
