# some self explanatory recursion implementations
# each of them have a base case which is equivalent to the termination condition in a while loop
# if it is not specified correctly the program might run into an infinite recursion

# n! = n x (n-1)!
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# m x n = m + (m x (n-1))
def multiply(m, n):
    if n == 1:
        return m
    else:
        return m + multiply(m, n-1)

# len(list) == 1 + len(list[1:])
def listLen(l):
    if l == []:
        return 0
    else:
        return 1 + listLen((l[1:]))

# sum(list) == list[0] + sum(list[1:])
def listSum(l):
    if l == []:
        return 0
    else:
        return l[0] + listSum(l[1:])

print(factorial(5))
print(multiply(5,8))
print(listLen([1,7,0,8,13,45]))
print(listSum([1,7,0,8,13,45]))
