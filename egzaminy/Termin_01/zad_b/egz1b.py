# Dominik Szot

# Sprawdzam ile liści znajduje się na danym poziomie 
# wyszukuję najszerszego przedziału 
# należy usunąć wszystkie krawędzie o poziomie o jeden większym od poziomu najszerszego + wszystkie liście 
# występujące na poziomach mniejszych od poziomu najszerszego

# Niestety usuwa za dużo - są to krawędzie podrzewa którego liście nigdy nie dosięgną poziomu który będzie najszerszy

# o(n^2)


from collections import deque
from egz1btesty import runtests

class Node:
  def __init__( self ):
    self.left = None    # lewe poddrzewo
    self.right = None   # prawe poddrzewo
    self.x = None       # pole do wykorzystania przez studentow

def Bfs(T, X, D):
  q = deque()
  T.x = 0
  q.appendleft(T)
  
  while q:
    u = q.pop()
    if u.left is not None and u.left.x is None:
      u.left.x = u.x + 1
      X[u.x+1] += 1
          
      if u.left.left is None and u.left.right is None:
        D[u.x+1] += 1
                
      q.appendleft(u.left)
    if u.right is not None and u.right.x is None:
      u.right.x = u.x + 1
      X[u.x+1] += 1
      if u.right.left is None and u.right.right is None:
        D[u.x+1] += 1
      q.appendleft(u.right)

def wideentall( T ):
  result = 0
  matrix = []
  X = [0]*1000
  D = [0]*1000
  V = [0]*1000
  Bfs(T, X, D)
  
  max_d = 0
  max_ind = 0
    
  for i in range(len(X)):
    if X[i] > max_d:
      max_d = X[i]
      max_ind = i
  
  #print(X, max_ind, max_d)

  result = X[max_ind+1]
  result += sum(D[0:max_ind])
  return result
        
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( wideentall, all_tests = True )