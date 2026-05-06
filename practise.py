def sum_n(n):
    if n == 0:
        return 0
    else:
        sum = n + sum_n(n-1)
    return sum
print(sum_n(3))