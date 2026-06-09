# Explain list, dictionary, set , and generator comprehensions with examples.

# List comprehension

'''
List Comprehension is a concise way to create list in python by writing a loop and optional condition inside square brackets in a single line of code.
Example:
[expression for item in iterable if condition]
'''
numbers = [1, 2, 3, 4, 5]

squared_nums = [i ** 2 for i in numbers]
print(squared_nums)  # Output: [1, 4, 9, 16, 25]

# Dictionary comprehension

'''
Dictionary Comprehension is a concise way to create dictionary in python by writing a loop and optional condition inside curly braces in a single line of code.
Example:
{key_expression: value_expression for item in iterable if condition}
'''
dict_comprehension = {i: i ** 2 for i in numbers}
print(dict_comprehension)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Set comprehension
'''
Set Comprehension is a concise way to create set in python by writing a loop and optional condition inside curly braces in a single line of code.
Example:
{expression for item in iterable if condition}
'''
set_comprehension = {i ** 2 for i in numbers}
print(set_comprehension)  # Output: {1, 4, 9, 16, 25}

# Generator comprehension
'''
Generator Comprehension is a concise way to create generator in python by writing a loop and optional condition inside parentheses in a single line of code.
Example:
(expression for item in iterable if condition)
'''
generator_comprehension = (i ** 2 for i in numbers)
print(list(generator_comprehension))  # Output: [1, 4, 9, 16, 25]
