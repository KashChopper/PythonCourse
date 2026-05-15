"""
A generator in python is a special function that produces value one by one using the yield keyword instead of returning all the values at once.
 Generators helps us to generate a value on the fly rather than create and store the entire sequence in memory like list, tuple etc
"""
number = 3
def number_generator(number):
    for i in range(number):
        yield i

gen = number_generator(number)
print(next(gen))
print(next(gen))   

# OR 

for j in gen:
    print(j)