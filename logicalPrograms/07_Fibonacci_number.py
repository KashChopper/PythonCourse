print("Method 1")

num = 10
a = 0
b = 1
for i in range(num):
    print(a, end= " ")
    temp = a
    a = b
    b = temp + b
    

print("Method 2")
n = 10

a, b = 0, 1

for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
print("")
print("Method 3")

# Using recursion (slow)

def fib(num):
    if num < 1:
        return num
    return(fib(num-1)+fib(num-2))
fib(3)