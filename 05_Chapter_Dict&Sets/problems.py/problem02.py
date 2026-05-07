"""
Write a program to input eight numbers from the user and display all the unique
numbers (once).

"""
num_list = set()

for i in range(1,9):
    num = input(f"Enter the {i} number: ")
    num_list.update(num)
print(num_list)
