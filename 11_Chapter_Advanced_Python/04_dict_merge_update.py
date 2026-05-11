"""
Definition of dict merge and update in Python.
In Python, you can merge two dictionaries using the `update()` method or the `|` operator (available in Python 3.9 and later). The `update()` method modifies the original dictionary in place, while the `|` operator creates a new dictionary that combines the two.
"""

# Using the update() method
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
dict1.update(dict2)
print("After using update():", dict1)  # Output: {'a': 1, 'b': 3, 'c': 4}

# Using the | operator (Python 3.9+)
dict3 = {'a': 1, 'b': 2}
dict4 = {'b': 3, 'c': 4}
merged_dict = dict3 | dict4
print("After using | operator:", merged_dict)  # Output: {'a': 1, 'b': 3, 'c': 4}

# Note: The `|` operator does not modify the original dictionaries, while `update()` does.
# Using the ** unpacking operator (Python 3.5+)
# it is useful for merging dictionaries in a more concise way, especially when you want to create a new dictionary without modifying the originals.
dict5 = {'a': 1, 'b': 2}
dict6 = {'b': 3, 'c': 4}
merged_dict_unpacking = {**dict5, **dict6}
print("After using ** unpacking operator:", merged_dict_unpacking)  # Output: {'a': 1, 'b': 3, 'c': 4}