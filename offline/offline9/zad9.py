# Dominik Szot

# Algorytm Edmondsa-Karpa z wyborem dwóch miast posortowanych pod względem przepustowości

# złożoność czasowa O(VE^2 * V^2)


import math
from zad9testy import runtests
from collections import deque

def BFS(G, s, t, parent):
    n = len(G)
    visited = [False]*n

    q = deque()
    q.append(s)

    visited[s] = True
    

    while q:
        u = q.pop()
        for i in range(n):
            if visited[i] == False and G[u][i] > 0:
                q.append(i)
                visited[i] = True
                parent[i] = u
    
    return visited[t] == True
        
    
def FordFulkerson(G, s, t):
    n = len(G)
    parent = [-1] * n
    max_flow = 0
    
    while BFS(G, s, t, parent):

        path_flow = math.inf
        x = t
        while x != s:
            u = parent[x]
            path_flow = min(path_flow, G[u][x])
            x = parent[x]

        max_flow += path_flow

        y = t
        while y != s:
            u = parent[y]
            G[u][y] -= path_flow
            G[y][u] += path_flow
            y = parent[y]
    
    return max_flow


def highway( G,s ):
    n1 = max(G, key=lambda x: x[0])[0]
    n2 = max(G, key=lambda x: x[1])[1]
    n = max(n1,n2) + 1

    graph = [[0 for _ in range(n)] for _ in range(n)]
    test = [[0, i] for i in range(n)]

    for i in G:
        graph[i[0]][i[1]] = i[2]
        test[i[1]] = (test[i[1]][0] + i[2], i[1])
    
    max_flow = 0
    
    test = sorted(test, key=lambda x: x[0], reverse=True)

    for v1, i in test:
        if i != s:
            
            graph_copy = [j[:] for j in graph] 
            m1 = FordFulkerson(graph_copy, s, i)
            
            if max_flow//2 > m1:
                return max_flow
            
            for v2, j in test[:i]: 
                if j != s and j != i: 
                    
                    if max_flow > v1 + v2:
                        return max_flow
                    
                    graph_copy_copy = [j[:] for j in graph_copy] 
                    m2 = FordFulkerson(graph_copy_copy, s, j)
                    max_flow = max(m2+m1, max_flow)

    
    return max_flow


    
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( highway, all_tests = True )