import sys
from randomize import *

sys.setrecursionlimit(100000)

def quicksort(A, l, r):
    if r-l <= 1:
        return ()

    yellow = l + 1
    for green in range(l+1, r):
        if A[green] <= A[l]:
            A[yellow], A[green] = A[green], A[yellow]
            yellow += 1

    A[l], A[yellow-1] = A[yellow-1], A[l]
    quicksort(A, l, yellow-1)
    quicksort(A, yellow, r)

a = list(range(100000, 1, -1))
randomize(a)
quicksort(a, 0, len(a))
print(a)