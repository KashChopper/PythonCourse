"""
4. Write a program to find whether a given number is prime or not.

"""

number = int(input("Enter the number: "))

for i in range(2, number):
    if number % i == 0:
        print(f"{number} is composite")
        break
    else:
        print(f"{number} is prime")


