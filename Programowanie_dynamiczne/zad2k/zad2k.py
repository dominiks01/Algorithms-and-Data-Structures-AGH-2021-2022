from curses import endwin
import re
from zad2ktesty import runtests

def palindrom( S ):
    array = [[0 for _ in range(len(S)+1)] for _ in range(len(S)+1)]
    S_reversed = S[::-1]

    max_l = 0
    ending = 0

    for i in range(1, len(S)+1):
        for j in range(1, len(S)+1):
            if S[j-1] == S_reversed[i-1]:
                array[i][j] = array[i-1][j-1] + 1

                if array[i][j] > max_l:
                    max_l = array[i][j]
                    ending = i
            
  
    return S[ending - max_l : ending]

runtests ( palindrom )