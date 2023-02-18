# Rozwiązanie polega na posortowaniu przedziałów względem pierwszej wartości i 
# siłowym sprawdzaniu wszystkich przedziałów zawartych w aktualnie sprawdzanym przedziale 

# Złożoność O(N**2), gdzie n - liczba przedziałów 

# W celu usprawnienia algorytmu w momencie porównywania przedziałów wybierany jest następny 
# kandydat na przedział zawierający więcej przedziałów (będzie on pierwszym przedziałem który kończy się dalej od aktualnego)


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
    quick_sort(L, 0, len(L)-1)
    result = 0
    i = 0
    act = 0 
    
    while i < len(L): 
        
        j = i + 1
        firstToCheck = 0

        while j < len(L) and L[i][1] >= L[j][0]:     
            if L[i][1] >= L[j][1]:
                act += 1
            elif firstToCheck == 0:
                firstToCheck = j
            j += 1

        if j > len(L):
            return max(result, act)

        i = firstToCheck
        result = max(result, act)

        if firstToCheck == 0:
            break

        act = 0 
        
        # Elementy które zaczynają się w tym samym punkcie a które mogą być pomijane przy 
        # dobieraniu kandydata => Wszystkie elementy które zaczynają się w tym 
        # samym punkcie co kandydat, są mniejsze od aktualnie sprawdzanego przedziału,
        # zostały umiejscowione przed kandydatem w posortowanej tablicy 
        
        j = firstToCheck - 1 
        while L[j][0] == L[i][0]:
            j -= 1 
            act += 1
            
        
        
    return result
    

runtests( depth ) 
