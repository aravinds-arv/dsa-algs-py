def square(x):
    return x*x

def isEven(n):
    return n%2 == 0

lc = [square(x) for x in range(100) if isEven(x)]
print(lc)