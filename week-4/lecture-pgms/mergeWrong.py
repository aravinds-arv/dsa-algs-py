def merge(A, B):
    C, m, n = [], len(A),len(B)
    i, j = 0, 0
    while i + j < m + n:
        print(m,n,i,j)
        if i == m or A[i] > B[j]:
            C.append(B[j])
            j += 1

        elif j == n or A[i] <= B[j]:
            C.append(A[i])
            i += 1
    
    return C

A = [2,4,6]
B = [1,3,5]
print(merge(A, B))
print(len(merge(A, B)))