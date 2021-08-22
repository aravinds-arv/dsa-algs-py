# using previously created factors() to return factorList
def factors(n):
    factorList = []
    for i in range(1,n+1):
        if n%i == 0:
            factorList.append(i)
    return factorList

# a prime nummber has only two factors which are 1 and itself
def isPrime(n):
    return factors(n) == [1,n]

print(isPrime(32))
print(isPrime(31))
print(isPrime(1)) # boundary condition yet works fine