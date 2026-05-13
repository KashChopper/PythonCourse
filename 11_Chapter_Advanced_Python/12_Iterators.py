"""
An iterator is an object that contains a countable number of values.
Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__().
Python collections like:

list
tuple
set
dictionary
string

are iterable objects.

Iterator helps access their elements sequentially.

"""
l = [1, 2, 3, 4, 5]

x = iter(l)
print(next(x))