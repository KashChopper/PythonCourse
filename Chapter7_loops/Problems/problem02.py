"""
2. Write a program to greet all the person names stored in a list ‘l’ and which starts
with A.
l = ["Aasif", "Ayan", "Athar", "Musa"]

"""
l = ["Aasif", "Ayan", "Athar", "Musa"]

for name in l:
    if name.startswith("A"):
        print(f"Assalmualikum {name}")

