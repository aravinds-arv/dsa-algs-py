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

A = list(range(0, 100, 2))
B = list(range(1, 75, 2))
print(merge(A, B))
print(len(merge(A, B)))