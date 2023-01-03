from hashlib import new
from egz3btesty import runtests


def maze( L ):

    new_array = [[0 for _ in range(len(L))] for _ in range(len(L))]

    
    for i in new_array:
        print(i)

    return 0


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maze, all_tests = False )
