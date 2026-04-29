"""
if:
    if statement executes the block of code only when the condition is true
"""
age = 55
if age >= 18:
    print("You are eligible to vote.")

"""
if-else statement:
    if the condition evaluates true then the if body will be executed, otherwise the else body will be executed.
"""
# example

age = 20
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")


"""
if-elif-else statement:
    if the first condition is false, it checks the second condition, and so on.
"""
# example

age = 20
if age < 18:
    print("You are a minor.")
elif age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")
