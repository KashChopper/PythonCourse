nums = [4,2,3,4]


def is_triangle(a,b,c):
    if a+b>c and b+c>a and c+a>b:
        return True
    return False

count = 0
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        for k in range(j+1, len(nums)):
            if is_triangle(nums[i], nums[j], nums[k]):
                count += 1


print(count)


