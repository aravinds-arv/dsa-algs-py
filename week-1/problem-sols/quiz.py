# 1. What is the value of g(728) for the function below? 

def g(y):
    b = 0
    while y >= 3:
        (y,b) = (y/3,b+1)
    return(b)

# Ans: 5


# 2. What is f(90)-f(89), given the definition of f below? 

def f(n):
    s = 0
    for i in range(2,n):
        if n%i == 0 and i%2 == 1:
            s = s+1
    return(s)

# Ans: 5


# 3. Consider the following function h.

def h(n):
    s = True
    for i in range(1,n+1):
        if i*i == n:
            s = False
    return(s)

# The function h(n) given above returns False for a positive number n if and only if:
# Options:-
    # n is an odd number.
    # n is a prime number.
    # n is a perfect square.
    # n is a composite number

# Ans: n is a perfect square.


# 4. Consider the following function foo.

def foo(m):
    if m == 0:
      return(0)
    else:
      return(m+foo(m-1))

# Which of the following is correct?
# Options:-
    # The function always terminates with f(n) = factorial of n
    # The function always terminates with f(n) = n(n+1)/2
    # The function terminates for non­negative n with f(n) = factorial of n
    # The function terminates for non­negative n with f(n) = n(n+1)/2 

# Ans: The function terminates for non­negative n with f(n) = n(n+1)/2 