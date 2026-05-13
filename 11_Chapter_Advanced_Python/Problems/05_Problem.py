# write a program to filter a list of numbers which are divisible by 5 

nums = [2,5,6,10,34,35,90]

def five(n):
    if n % 5 == 0:
        return True
    return False

five_divisible = filter(five, nums)

print(list(five_divisible))