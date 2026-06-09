'''
List comprehensions are a concise way to create lists in Python by writing a loop and optional condition inside square brackets in a single line of code. They can be used to create new lists by applying an expression to each item in an iterable, optionally filtering items with a condition.
'''
my_list = [2,3,5,6,6]

# making a new list with the square of each element in my_list
squared_list = [i **2 for i in my_list]
print(squared_list)  # Output: [4, 9, 25, 36, 36]