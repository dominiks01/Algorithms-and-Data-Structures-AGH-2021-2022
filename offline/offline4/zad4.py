
# Algorytm Knapsack do znajowania najbardziej korzystnego ustawienia budynków.
# Sortujemy tablicę względem końca budynku. 

# Przechodzimy przez tablicę F odnajdując numery budynków użytych w najbardziej opłacalnej konfiguracji.
# Budynek jest użyty gdy zmienia się pojemność przy tej samej/lepszej opłacalności 

# Sformułowanie rekurencyjne:
# f(i, b) =  max(f(i-1, b), f(j, b - W(i)) + p(i)), j <= i-1

# Złożoność obliczeniowa:
# O(n^2) 


from zad4testy import runtests

def select_buildings(T,p):

    # Tablica z indeksami aby móc znaleźć pozycję budynku w nieposortowanej tablicy
    T_cpy = [(T[i], i) for i in range(len(T))]      
    T_cpy = sorted(T_cpy, key=lambda x: x[0][2])
    T = [x[0] for x in T_cpy]

    n = len(T)
    F = [[0 for b in range(p+1)] for i in range(n)]

    for b in range(T[0][3], p+1):
        F[0][b] = (T[0][2] - T[0][1])*T[0][0]

    # Algorytm knapsack 
    for b in range(p+1):
        for i in range(1, n):
            F[i][b] = F[i-1][b]
            if b - T[i][3] >= 0:
                j = i-1
                while T[j][2] >= T[i][1] and j > 0:
                    j -= 1

                if j == 0 and T[j][2] >= T[i][1]:
                    # gdy wszystkie konfiguracje nachodzą na nasz sprawdzany
                    F[j][b] = 0
                    

                F[i][b] = max(F[i][b], F[j][b-T[i][3]]+(T[i][2]-T[i][1])*T[i][0])
    
    b = p
    result = []
    value = F[n-1][p]

    # Różnica w pojemości bez negatywnej zmiany opłacalności oznacza użycie danego budynku 
    for i in range(n-1, 0, -1):
        if value <= 0:
            break
        if F[i][b] <= value and F[i][b] > F[i-1][b]:
            result.append(T_cpy[i][1])
            value -= (T[i][2]-T[i][1])*T[i][0]
            b -= T[i][3]
    
    # warunek brzegowy: sprawdzamy czy budynek 0 jest używany
    if value != 0:
        result.append(T_cpy[0][1])  

    return result

runtests( select_buildings )