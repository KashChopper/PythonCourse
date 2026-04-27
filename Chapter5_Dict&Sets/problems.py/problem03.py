"""

1. Create an empty dictionary. Allow 4 friends to enter their favorite language as
value and use key as their names. Assume that the names are unique.
2. If the names of 2 friends are same; what will happen to the program in problem 1?

it will update 1 and display one key

2. If languages of two friends are same; what will happen to the program in problem 1
it will print the values 

"""
d = {}
for i in range(1, 5):
    name = input("Enter the name: ")
    language= input("Enter the language: ")
    d.update({name: language})
print(d) 