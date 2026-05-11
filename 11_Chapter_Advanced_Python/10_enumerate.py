l = [3, 5, 6, 7, 9]
index = 0
for item in l:
    print(f"The item number at index {index} is {item}")
    index += 1

# This can be simplified using enumerates function

for index, item in enumerate(l):
    print(f"The item number at index {index} is {item}")