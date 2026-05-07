"""
Write a python function to print first n lines of the following pattern:
***
** - for n = 4
*
"""
def pattern(n):
    for i in range(n,0,-1):
        print("*" *i)

pattern(5)

# Recursive method

def ptrn(n):
    if n == 0:
        return
    else:
        print("*" * n)
        ptrn(n-1)

ptrn(5)