"""
Exception handling in Python allows you to manage errors gracefully without crashing your program. You can use try-except blocks to catch and handle exceptions, ensuring that your code continues to run smoothly even when unexpected issues arise.
"""

try:
    num = int(input("Enter the number: "))
    print(num)

except Exception as e:
    print(e)

print("Thanks")  # finally block is used especially with the functions or methods

