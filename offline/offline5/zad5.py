# Algorymt przechodzi maksymalną ilość dostępnych pól a następnie wybiera plamę z maksymalną
# ilością paliwa którą ma za sobą (lub tę na której aktualnie stoi). 

# Wartości pól przetrzymuję w Kolejce priorytetowej
# Dla ułatwienia mnożę warości dodawane do kolejki przez (-1)

# Złożoność algorytmu O(nlogn)

from zad5testy import runtests
from queue import PriorityQueue

def plan(T):
    result = [0]
    sum_t = T[0]
    last = 1

    P = PriorityQueue()

    while sum_t < len(T) - 1:
        for i in range(last, sum_t+1):
            P.put((-T[i], i)) 
        last = sum_t+1
        act = P.get()
        sum_t -= act[0]
        result.append(act[1])

    return sorted(result)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( plan, all_tests = True )