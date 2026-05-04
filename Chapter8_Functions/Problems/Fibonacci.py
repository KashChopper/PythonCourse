def fibonacci(n):
    a = 0
    b = 1
    for _ in range(n):
        sum = a + b
        a = b
        b = sum

    return a

print(fibonacci(6))

def fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
        a,b = b, a+b
    return a

print(fibonacci(6))