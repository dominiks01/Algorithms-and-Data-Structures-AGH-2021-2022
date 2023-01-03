# Algorytm BFS
# Jeśli istnieje krawędź w grafie której usunięcie wydłuży najkrótszą ścieżkę to:
# - wszystkie najkrótsze ścieżki spotykają się w jednym wierzchołku,
# - do tego wierzchołka prowadzi tylko i wyłącznie jedna krawędź o czasie (odległości) mniejszym o 1 

# Algorytm ma za zadanie sprawdzić czy istnieje taka krawędź, a jeśli tak to ją znaleźć

# O(E + V + Q), gdzie Q jest najkrótszą ścieżką

from zad6testy import runtests
from collections import deque

def longer( G, s, t ):

   visited = [False]*len(G)
   times = [None]*len(G)
   Q = deque()

   times[s] = 0
   visited[s] = True

   Q.append(s)

   while Q:
      u = Q.popleft()
      for i in G[u]:
         if not visited[i]:
            visited[i] = True
            times[i] = times[u] + 1
            Q.append(i)

   if times[t] is None:
      return None

   if times[t] == times[s] + 1:
      return (s,t)

   P = deque()

   for i in G[t]:
      if times[i] < times[t]:
         P.append(i)

   while P:
      u = P.popleft()
      if not P and u != 0:
         qq = deque()   # kolejka przechowywująca czasy/odległości 
         for i in G[u]:
            if times[i] + 1 == times[u]:
               P.append(i)
               qq.append(times[i])
         if qq.count(times[u]-1) == 1: # jeśli istnieje tylko 1 wierzchołek z czasem mniejszym o 1, od jedynego wierzchołka
            z = P.popleft()
            return (z, u)
      else:
         for i in G[u]:
            if times[i]+1 == times[u] and P.count(i) == 0:
               P.append(i)

   return None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( longer, all_tests = True)
