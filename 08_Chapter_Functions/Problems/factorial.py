"""
factorial.py
The factorial of a non-negative integer n is the product of all positive integers less than or equal to n. It is denoted by n!. For example, 5! = 5 * 4 * 3 * 2 * 1 = 120. The factorial function can be defined recursively as follows:
- factorial(0) = 1
- factorial(n) = n * factorial(n - 1) for n > 0
example:
factorial(3) = 3 * 2 * 1 = 6
factorial(0) = 1
"""
# factorial of a number using recursion
def factorial(n):
    if n == 0:
        return 1
    elif n < 0:
        return "Factorial not defined for negative numbers"
    else:
        return n * factorial(n - 1)
num = int(input("Enter the number: "))

print(factorial(num))
    

# factorial using simple iterative method

def fact(n):
    if n < 0:
        return "Factorial not defined for negative numbers"
    elif n == 0:
        return 1
    else:
        result =1
        for i in range(1, n+1):
            result *= i
        return result
print(fact(num))

# Using for loop 
fact = 1
for i in range(1, num+1):
    fact = fact * i
print(fact)