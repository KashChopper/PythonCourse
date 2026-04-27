"""
In python tuple is an ordered, immutable collection used to store multiple items/values in a single variable.
"""
cars_tuple = ("Toyota", "Honda", "Ford", "BMW", "Mercedes")

# Accessing tuple elements
print(cars_tuple[0])    # Accessing the first item
print(cars_tuple[1])    # Accessing the second item
print(cars_tuple[-1])   # Accessing the last item
print(cars_tuple[::-1])  # Accessing the tuple in reverse order
print(cars_tuple[1:4])   # Accessing a slice of the tuple

# Tuples are immutable, so we cannot change, add, or remove items

"""
Methods available for tuples
As the tuple are immutable, they have two main methods:
1. count(item) - Returns the number of occurrences of an item in the tuple.
2. index(item) - Returns the index of the first occurrence of an item in the tuple.
"""

v1 = cars_tuple.count("Toyota")  # Counting occurrences of "Toyota"
v2 = cars_tuple.index("Honda")  # Finding the index of "Honda"

print(v1,v2)