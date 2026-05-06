# Write a python function to remove a given word from a list

def rem(l, word):
    for i in l:
        l.remove(word)
        return l
l = ["aasif", "ayan", "athar", "an"]

print(rem(l, "an"))