
def approach1(name: str):
    if name == name[:: -1]:
        print("Palindrome")
    else:
        print("Not palindrome")

approach1("mam")


def approach2(name: str):
    reverse_string = "".join(reversed(name))
    if name == reverse_string:
        print("Palindrome")
    else:
        print("Not palindrome")

approach2("mam")