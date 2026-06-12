name = "John"
# Approach 1
reverse_name = name[:: -1]

print(reverse_name)

# Approach 2

reverse_name1 = reversed(name)
# It returns a reversed iterator object. Covert it to a sting
print("".join(reverse_name1))