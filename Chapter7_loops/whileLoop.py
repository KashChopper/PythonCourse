"""
In while loops, the condition is checked first if it evaluates to true, then the body. of the loop gets executed

SYNTAX
while(condition):
    statement
"""

i = 0
while i <= 5:
    print(i)
    i = i+1
print("Loop ended")
l = [2, 5, "aasif", 6.5]
item = 0
while item < len(l):
    print(l[item])
    item += 1
print("Loop ended")