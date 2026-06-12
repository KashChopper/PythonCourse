
n = 4
fact = 1

for i in range(1, n+1):
    result = fact * i
    fact = result
print(fact)