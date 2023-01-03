from hashlib import new
from egz3atesty import runtests

def snow( T, I ):
    # tu prosze wpisac wlasna implementacje
    p_array = []

    result = 0
    max_value = 0

    for x,y in I:
        p_array.append((x, 1))
        p_array.append((y, -1))
    
    p_array = sorted(p_array, key=lambda x: x[0])
    
    for _, value in p_array:
        result += value
        max_value = max(max_value, result)

    return max_value

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = True )
