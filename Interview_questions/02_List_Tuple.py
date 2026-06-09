

# what is list in python?

"""
A list in python is an ordered, mutable collection used to store multiple items/values in a single variable.

Key features:
1. Ordered: The items in a list have a defined order, and that order will not change unless you explicitly reorder the list.
2. Mutable: You can change, add, or remove items from a list after it has been created.
3. Allows Duplicates: Lists can contain multiple instances of the same value.
4. Dynamic Size: Lists can grow and shrink in size as needed.
5. Heterogeneous: Lists can contain items of different data types.
6. Memory Usage: Consumes more memory than tuples due to their mutability and dynamic nature.

"""
my_list = [1, "Hello", 3.14, True, [1, 2, 3], (4, 5), {"key": "value"}]



# what is tuple in python?

"""
In python tuple is an ordered, immutable collection used to store multiple items/values in a single variable.

Key features:
1. Ordered: The items in a tuple have a defined order, and that order will not change unless you explicitly reorder the tuple.
2. Immutable: Once a tuple is created, you cannot change, add, or remove items from it.
3. Allows Duplicates: Tuples can contain multiple instances of the same value.
4. Dynamic Size: Tuples can grow and shrink in size as needed.
5. Heterogeneous: Tuples can contain items of different data types.
6. Memory Usage: Consumes less memory than lists due to their immutability and fixed nature.
"""

my_tuple = (1, "Hello", 3.14, True, [1, 2, 3], (4, 5), {"key": "value"})