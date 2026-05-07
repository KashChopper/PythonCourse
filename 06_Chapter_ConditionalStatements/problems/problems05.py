# Write a program which finds out whether a given name is present in a list or not.

num_list = [2,4,5,6,7,8,9,11]

num = int(input("Enter the number: "))

if num in num_list:
    print("The number is present in the list")
else:
    print("The number is not present in the list")