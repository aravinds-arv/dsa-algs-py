m = int(input())
n = int(input())

def gcd(m,n):

    #assuming m >= n
    m,n = max(m,n),min(m,n)

    while m%n != 0:
        #just to make sure m is actually >= n
        m,n = max(n,m-n),min(n,m-n)
    return n

print(gcd(m,n))