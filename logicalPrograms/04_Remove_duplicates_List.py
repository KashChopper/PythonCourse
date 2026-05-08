nums = [0,1,2,3,4,5,3,2,4]
unique = []

for i in nums:
    if i not in unique:
        unique.append(i)

print(unique)