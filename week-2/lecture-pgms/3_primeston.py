# using previouly defined factor() and isPrime()
def factors(n):
    factorList = []
    for i in range(1,n+1):
        if n%i == 0:
            factorList.append(i)
    return factorList

def isPrime(n):
    return factors(n) == [1,n]

def primesUpto(n):
    primeList = []
    for i in range(1,n+1):
        if isPrime(i):
            primeList.append(i)
    return primeList

print(primesUpto(64))