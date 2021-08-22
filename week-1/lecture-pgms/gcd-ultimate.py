m = int(input())
n = int(input())

def gcd(m,n):
    #assuming m >= n
    if n > m:
        m,n = n,m

    #replacable
    if m%n == 0:
        return n
    else:
        return gcd(n,m%n) #need not bother about m >= n bcoz it is always

    #you can replace the code after '#replacable' with below code
    #both does the same thing

    # while m%n != 0:
    #     m,n = n,m%n
    # return n

print(gcd(m,n))