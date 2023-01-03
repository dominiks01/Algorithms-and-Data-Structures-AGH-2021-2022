# Algorytm sprawdza wszystkie możliwe drogi przechodzące przez wszystkie miasta do miasta początkowego

# złożoność czasowa O(n^3)
# złożoność pamięciowa O(n)

from zad7testy import runtests
from collections import deque


def _droga(visited, q, i, G): 
    if i == 0:                                          
        u = q.pop()
        if u == accepted:
            return all(x == True for x in visited[1:]) 
        return False

    visited[i] = True
    u = q.pop()

    for j in u:
        if visited[j] == False:
            if i in G[j][0]:
                q.append(G[j][1])
            else:
                q.append(G[j][0])
            h.append(j)
            if _droga(visited, q, j, G):
                return True
            h.pop()
        
    visited[i] = False
    return False

h = deque()
accepted = []

def droga( G ):
    # tu prosze wpisac wlasna implementacje
    q = deque()
    visited = [False for _ in range(len(G))]

    global h, accepted
    h.clear()
    accepted.clear()
    u = G[0][0] + G[0][1]

    for i in u:
        h.append(i)

        if 0 in G[i][0]:                # dodaję jedynie miasta z dostępnej bramy 
            q.append(G[i][1])
        else:
            q.append(G[i][0])

        if i in G[0][0]:
            accepted = G[0][0]
        else:
            accepted = G[0][1]

        if _droga(visited, q, i, G):
            return list(h)
        h.pop()
  

    return None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( droga, all_tests = True )
