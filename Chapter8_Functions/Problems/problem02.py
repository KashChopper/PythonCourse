"""
Write a python function to print first n lines of the following pattern:
***
** - for n = 4
*
"""
def star(n):
    for i in range(n, 0, -1):
        print("*" * i) 
print(star(4))
