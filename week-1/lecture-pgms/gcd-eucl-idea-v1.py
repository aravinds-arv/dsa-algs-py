m = int(input())
n = int(input())

def gcd(m,n):
    
    #assuming m >= n
    m,n = max(m,n),min(m,n)
    if m%n == 0:
        return n

    else:
        #just to make sure m is actually >= n
        return gcd(max(n,m-n),min(n,m-n))

print(gcd(m,n))