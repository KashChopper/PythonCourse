"""
DataTypes are used to define different types of data
Python provides build in dataTypes such as numeric (int, float, complex), Sequence (List, Tupple, range), mapping(dict), Set(set, frozenset), text (str), boolean (bool), binanry (bytes, bytearray) and noneType

Built - in - types
Numeric     -->     int, float, complex
boolean     -->     bool
string      -->     str
sequence    -->     list, tupple, range
mapping     -->     dict
set         -->     set, frozenset
binary      -->     byte, bytearray, memoryview
none        -->     noneType


"""


# Numeric type 
a = 10
b = 3.14
c = 3 + 2j
print(type(a))  # Output: <class 'int'>
print(type(b))  # Output: <class 'float'>
print(type(c))  # Output: <class 'complex'>

# Boolean type
is_valid = True
is_empty = False
print(type(is_valid))  # Output: <class 'bool'>
print(type(is_empty))  # Output: <class 'bool'>

# String type
name = "John Doe"
print(type(name))  # Output: <class 'str'>

# Sequence type
my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)
my_range = range(1, 10)
print(type(my_list))  # Output: <class 'list'>
print(type(my_tuple))  # Output: <class 'tuple'>
print(type(my_range))  # Output: <class 'range'>

# Mapping type
my_dict = {"name": "John", "age": 30, "city": "New York"}
print(type(my_dict))  # Output: <class 'dict'>

# Set type
my_set = {1, 2, 3, 4, 5}
my_frozenset = frozenset([1, 2, 3, 4, 5])
print(type(my_set))  # Output: <class 'set'>
print(type(my_frozenset))  # Output: <class 'frozenset'>


# Binary type
my_bytes = b"Hello, World!"
my_bytearray = bytearray(b"Hello, World!")
print(type(my_bytes))  # Output: <class 'bytes'>
print(type(my_bytearray))  # Output: <class 'bytearray'>

# NoneType
my_none = None
print(type(my_none))  # Output: <class 'NoneType'>