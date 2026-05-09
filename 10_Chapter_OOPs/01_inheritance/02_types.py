"""
TYPES OF INHERITANCE

1. SINGLE LEVEL INHERITANCE 

2. MULTIPLE INHERITANCE

3. MULTILEVEL INHERITANCE

4. HIERARCHICAL INHERITANCE

5. HYBRID INHERITANCE 

"""

# 1. SINGLE LEVEL INHERITANCE 

# In single level inheritance only two classes will participate. One will be parent class and other will be child class
print("___________________________SINGLE LEVEL INHERITANCE__________________________\n")
class Parent:
    print("I am parent class")


class Child(Parent):
    print("I am child class")

info = Child()


print("___________________________MULTIPLE INHERITANCE__________________________\n")

# 2. MULTIPLE INHERITANCE

# it is a type of inheritance where single child class will have multiple parent classes

class Father:
    print("I am father")

class Mother:
    print("I am mother")

class Child(Father, Mother):
    print("I am child")

c = Child()

print("___________________________MULTILEVEL INHERITANCE__________________________\n")

# 3. MULTILEVEL INHERITANCE

# In this type of inheritance more than two classes will participate. There will be atleast one class which behave as child class as parent class for other or another class

class GrandFather:
    print("I am grandfather")

class Parent(GrandFather):
    print("I am parent")

class child(Parent):
    print("I am child")


print("___________________________HIERARCHICAL INHERITANCE__________________________\n")

# 4. it is a type of inheritance where single parent class will have multiple child class 

class Parent:
    pass

class child1:
    pass

class child2:
    pass


print("___________________________HYBRID INHERITANCE__________________________\n")

# it is the combination of multiple and hierarchial inheritance 

class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B,C):
    pass

