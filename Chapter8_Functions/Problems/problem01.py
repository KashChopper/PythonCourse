# 4. Write a recursive function to calculate the sum of first n natural numbers.

def sum_n(n):
    if n == 1:  # To stop the recursion when n is 1, by which the recursion will not go to negative numbers and will return the sum of first n natural numbers.
        return 1
    else:
        sum = n + sum_n(n-1)
    return sum
num = int(input("Enter the number: "))
print(sum_n(num))

# Using loop
sum = 0
for i in range(1,num+1):
    sum = sum + i
    
print(sum)


# Using function iterative method

def sum(n):
    if n < 1:
        return 0
    else:
        sum = 0
        for i in range(1, n+1):
            sum = sum + i
        return sum 
print(sum(num))
    


