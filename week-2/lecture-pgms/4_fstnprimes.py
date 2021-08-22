# using previouly defined factor() and isPrime()
def factors(n):
    factorList = []
    for i in range(1,n+1):
        if n%i == 0:
            factorList.append(i)
    return factorList

def isPrime(n):
    return factors(n) == [1,n]

def nPrimes(n):
    count, i, primeList = 0, 1, []
    while count != n:
        if isPrime(i):
            count += 1
            primeList.append(i)
        i += 1
    return primeList
print(nPrimes(5))