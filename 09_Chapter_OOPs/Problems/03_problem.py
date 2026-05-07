"""
Create a class with a class attribute a; create an object from it and set ‘a’
directly using ‘object.a = 0’. Does this change the class attribute?

"""

class test:
    a = 4

obj = test()
print(obj.a)  #4 prints the class attribute because instance attribute is not present
obj.a = 0   # instance attribute is set 
print(obj.a)  # 0  prints the instance attribute because instance attribute is present

print(test.a)  # 4 prints the class attribute