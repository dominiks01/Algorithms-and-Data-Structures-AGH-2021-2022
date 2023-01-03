# Dominik Szot

# rozwiązaniem jest pewna liczba ładunków śniegu
# przetrzymuję w kolejce wszystkie ładunki, wybieram naljepszy - najbardziej odpowiedni do momentu aż nie okaże się że wszystkie 
# pozostałe się stopiły 

# O(nlogn)

from egz1atesty import runtests
from collections import deque
from queue import PriorityQueue

def snow( S ):
  
    q = PriorityQueue()
    for i in S:
        q.put(-i)   

    i = 0
    result = 0
    while not q.empty():
        x = q.get()
        if x + i < 0:
            result += (x+i)
            i += 1
        if x + i >= 0:
            break
            
    return -result      
     
    

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = True )
