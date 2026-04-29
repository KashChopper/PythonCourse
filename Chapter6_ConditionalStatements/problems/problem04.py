# Write a program to find whether a given username contains less than 10
# characters or not.

user_name = input("Enter your username: ")
length = len(user_name)

if length < 10:
    print("Username contains less than 10 characters")
else:
    print("Username contains more than 10 characters")