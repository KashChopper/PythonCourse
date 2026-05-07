"""
Write a program to store seven fruits in a list entered by the user.
"""
fruit_list = []
f1 = input("Enter the fruit name number 1: ")
fruit_list.append(f1)
f2 = input("Enter the fruit name number 2: ")
fruit_list.append(f2)
f3 = input("Enter the fruit name number 3: ")
fruit_list.append(f3)
f4 = input("Enter the fruit name number 4: ")
fruit_list.append(f4)
f5 = input("Enter the fruit name number 5: ")
fruit_list.append(f5)
f6 = input("Enter the fruit name number 6: ")
fruit_list.append(f6)
f7 = input("Enter the fruit name number 7: ")
fruit_list.append(f7)

print(f"Your list of fruits is: {fruit_list}")


print("_________________________________________________________________________________________________________")
fruits = []

for i in range(1, 8):
    fruit = input(f"Enter the fruit name number {i}: ")
    fruits.append(fruit)

print(f"Your list of fruits is: {fruits}")
