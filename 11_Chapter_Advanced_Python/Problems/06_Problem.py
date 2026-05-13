from functools import reduce

# write a program to find the maximum of the numbers in a list using reduce method /


my_list = [12, 55, 554, 546]

def greater(a,b):
    if a>b:
        return a
    return b

max = reduce(greater, my_list)
print(max)