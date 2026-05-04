"""
Recursion is a programming technique where a function calls itself in order to solve a problem. It typically involves a base case that stops the recursion and a recursive case that breaks the problem into smaller subproblems.
"""

# Example of a recursive function to calculate the factorial of a number

def fact(n):
    if n == 0:
        return 1
    else:
        return n*fact(n-1)
number = int(input("Enter the number: "))
print(fact(number))
