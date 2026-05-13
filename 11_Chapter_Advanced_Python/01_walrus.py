'''
Walrus operator (:=) is a new assignment expression introduced in Python 3.8. It allows you to assign values to variables as part of an expression, which can help make your code more concise and readable.
'''

if (n := len("Hello, World!")) > 10:
    print(f"The length of the string is {n}, which is greater than 10.") 


if name:= input("Enter name: "):
    print(name)