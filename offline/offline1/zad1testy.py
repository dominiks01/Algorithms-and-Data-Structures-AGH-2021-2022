# zad1testy.py
from testy import *
from zad1test_spec import ALLOWED_TIME, TEST_SPEC

from copy import deepcopy


def copyarg( arg ):
    return deepcopy(arg)

def printarg(L, k):
    print(f"k: {k}")
    out = ', '.join([str(x) for x in L])
    print("Wejciowa lista:\t", limit(out))


def printhint( hint ):
    #out = ', '.join([str(x) for x in hint])
    print("Lista posortowana:\t", limit(hint))


def printsol( sol ):
    if sol is not None:
    #out = ', '.join([str(x) for x in sol])
        print("Wynik algorytmu:\t", limit(sol))

 
def check( l, k, hint, sol ):
    good = True
    for i in range(len(hint)):
        if (sol is not None and hint is not None) and sol[i] != hint[i]:
            print(f'Błąd! Nieprawidlowa liczba na pozycji {i}')
            good = False
            break
        elif sol is None or hint is None:
            return False

    return good


def gentest(k, n, maxint):
    l = [MY_random() % maxint for i in range(n)]
    l = sorted(l)
    pos = [i for i in range(n)]

    for i in range(n):
        if pos[i] != i: continue

        j = i + (MY_random() % (k+1))
        if j < n and pos[j] == j:
            tmp = l[i]
            l[i] = l[j]
            l[j] = tmp
            tmp = pos[i]
            pos[i] = pos[j]
            pos[j] = tmp

    arg = (l, k)
    hint = sorted(l)
    return arg, hint


def runtests( f ):
    TESTS = []
    for spec in TEST_SPEC:
        newtest = {}
        arg, hint = gentest(*spec)
        newtest["arg"] = arg
        newtest["hint"] = hint
        TESTS.append(newtest)

    internal_runtests( copyarg, printarg, printhint, printsol, check, TESTS, f, ALLOWED_TIME )

