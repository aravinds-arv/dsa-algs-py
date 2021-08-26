def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def multiply(m, n):
    if n == 1:
        return m
    else:
        return m + multiply(m, n-1)

def listLen(l):
    if l == []:
        return 0
    else:
        return 1 + listLen((l[1:]))

def listSum(l):
    if l == []:
        return 0
    else:
        return l[0] + listSum(l[1:])

print(factorial(5))
print(multiply(5,8))
print(listLen([1,7,0,8,13,45]))
print(listSum([1,7,0,8,13,45]))
