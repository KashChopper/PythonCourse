# def fibonacci(n):
#     a = 0
#     b = 1
#     for _ in range(n):
#         sum = a + b
#         a = b
#         b = sum

#     return a

# print(fibonacci(6))

# def fibonacci(n):
#     a = 0
#     b = 1
#     for i in range(n):
#         a,b = b, a+b
#     return a

# print(fibonacci(6))

# factorial of a number using recursion
# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
    
# number = int(input("Enter the number: "))
# print(fibonacci(number))

# factorial of a number using for loop

a = 0
b = 1
n = int(input("Enter the number: "))
for i in range(n):
    a,b = b, a+b
print(a)

