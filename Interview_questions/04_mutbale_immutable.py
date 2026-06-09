# What is the difference between mutable and immutable data types in Python?

'''
Mutable data types:
- Mutable data types are those that can be modified after their creation.
- Examples: List, Dictionary, Set
- Characteristics: Elements can be added, removed or changed.
'''
# List example
a_list = [1, 2, 3]
print("Original list:", a_list)
a_list.append(4)
print("Modified list:", a_list)

# Dictionary example
a_dict = {"name": "Aasif", "age": 24}
print("Original dictionary:", a_dict)
a_dict["age"] = 25
print("Modified dictionary:", a_dict)

'''
Immutable data types:
- Immutable data types are those that cannot be modified after their creation.
- Examples: String, Tuple, Frozen Set
- Characteristics: Once created, the value of the object cannot be changed.
'''


# String example
a_string = "Hello"
print("Original string:", a_string)
# Attempting to modify the string will create a new string
a_string = a_string + " World"
print("Modified string:", a_string)

# Tuple example
a_tuple = (1, 2, 3)
print("Original tuple:", a_tuple)
# Attempting to modify the tuple will create a new tuple
a_tuple = a_tuple + (4,)
print("Modified tuple:", a_tuple)

# Frozen Set example
a_frozenset = frozenset([1, 2, 3])
print("Original frozenset:", a_frozenset)
# Attempting to modify the frozenset will create a new frozenset
a_frozenset = a_frozenset.union([4])
print("Modified frozenset:", a_frozenset)
