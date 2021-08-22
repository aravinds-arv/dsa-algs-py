def factors(n):
    factorList = []
    for i in range(1,n+1):
        if n%i == 0:
            factorList.append(i)
    return factorList

print(factors(32))