"""
Write a program to detect double space in a string
"""

name = "Aasif is a  good  boy"

print(name.find("  ") != -1)
# or 

print(name.find("  "))

# OR 

print(name.count(" "))

# OR
if name.count(" ") > 1:
    print("Double space found")


# OR 

if "  " in name:
    print("Double space found")

# OR 

if name.find("  ") != -1:
    print("Double space found")