from functools import reduce

#Map example
"""Map function applies a function to all the items in an input list. It returns a map object (an iterator), which can be easily converted into a list."""
my_list = [3,5,6,2,7,8]
square = lambda x: x * x
square_list = map(square, my_list)
print(list(square_list))


# Filter example
"""
Filter function filters the items in an input list based on a condition. It returns a filter object (an iterator), which can be easily converted into a list.
"""
def even(n):
    if n % 2 == 0:
        return True
    return False

even_list = filter(even, my_list)

print(list(even_list))

# Reduce Example
"""Reduce function applies a rolling computation to sequential pairs of values in a list. It returns a single value that is the result of the reduction.
"""
def sum(a,b):
    return a + b

print(reduce(sum, my_list))

