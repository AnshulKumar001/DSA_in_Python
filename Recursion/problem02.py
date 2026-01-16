# Factorial of a Number using Recursion
def factorial(n):
    #base case
    if n==0 or n==1:
        return 1
    #recursive case
    return n*factorial(n-1)
print(factorial(5))