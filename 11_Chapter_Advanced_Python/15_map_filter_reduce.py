from functools import reduce

#Map example

my_list = [3,5,6,2,7,8]
square = lambda x: x * x
square_list = map(square, my_list)
print(list(square_list))


# Filter example
def even(n):
    if n % 2 == 0:
        return True
    return False

even_list = filter(even, my_list)

print(list(even_list))

# Reduce Example

def sum(a,b):
    return a + b

print(reduce(sum, my_list))

