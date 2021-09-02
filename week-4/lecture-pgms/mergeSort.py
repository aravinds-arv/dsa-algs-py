def merge(A, B):
    C, m, n = [], len(A),len(B)
    i, j = 0, 0
    while i + j < m + n:
        if i == m:
            C.append(B[j])
            j += 1

        elif j == n:
            C.append(A[i])
            i += 1
        
        elif A[i] <= B[j]:
            C.append(A[i])
            i += 1
        elif A[i] > B[j]:
            C.append(B[j])
            j += 1
    
    return C

def mergeSort(A, left, right):
    if right - left <= 1:
        return A[left:right]

    if right - left > 1:
        mid = (left + right)//2
        L = mergeSort(A, left, mid)
        R = mergeSort(A, mid, right)

        return(merge(L, R))

a = list(range(1 ,100000, 2)) + list(range(0, 100001, 2))
print(mergeSort(a, 0, len(a)))