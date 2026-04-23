"""
String Functions / Methods
Python provides many built-in string functions / methods to perform operations on strings such as length, case conversion, searching and much more
"""
"""
    Method                         purpose                                 example
1. Length
    len(string)                    Returns the length of a string       len("hello")  # 5
2. Case conversion
    string.upper()                 Converts a string to uppercase        "hello".upper()  # "HELLO"
    string.lower()                 Converts a string to lowercase        "HELLO".lower()  # "hello"
    string.capitalize()            Capitalizes the first character of a string     "hello".capitalize()  # "Hello"
    string.title()                 Converts the first character of each word to uppercase "hello world".title()  # "Hello World"
    string.swapcase()              Swaps the case of all characters in a string   "Hello World".swapcase()  # "hELLO wORLD"

3. Search and Check
    string.find(substring)          Returns the index of the first occurrence of a substring, or -1 if not found   "hello".find("e")  # 1
    string.startswith(prefix)       Checks if a string starts with a specified prefix       "hello".startswith("he")  # True
    string.endswith(suffix)         Checks if a string ends with a specified suffix       "hello".endswith("lo")  # True
    substring in string              Checks if a substring exists within a string       "e" in "hello"  # True

4. Replace and clean
    string.replace(old, new)        Replaces all occurrences of a substring with another substring   "hello".replace("e", "a")  # "hallo"
    string.strip()                   Removes whitespace from both ends     "  hello  ".strip()  # "hello"
    string.lstrip()                  Removes whitespace from the left end  "  hello  ".lstrip()  # "hello  "
    string.rstrip()                  Removes whitespace from the right end "  hello  ".rstrip()  # "  hello"

5. Validation methods
    string.isalnum()                Checks if all characters in a string are alphanumeric       "hello123".isalnum()  # True
    string.isalpha()                 Checks if all characters in a string are alphabetic        "hello".isalpha()  # True
    string.isdigit()                 Checks if all characters in a string are digits            "12345".isdigit()  # True
    string.isspace()                 Checks if all characters in a string are whitespace        "   ".isspace()  # True
    string.islower()                 Checks if all characters in a string are lowercase        "hello".islower()  # True
    string.isupper()                 Checks if all characters in a string are uppercase        "HELLO".isupper()  # True
    string.swapcase()              Swaps the case of all characters in a string   "Hello World".swapcase()  # "hELLO wORLD"

6. Alignment methods
    string.center(width)            Centers a string within a specified width       "hello".center(10)  # "  hello   "
    string.ljust(width)             Left-aligns a string within a specified width   "hello".ljust(10)  # "hello     "
    string.rjust(width)             Right-aligns a string within a specified width  "hello".rjust(10)  # "     hello"

7. Miscellaneous methods
    string.split(separator)         Splits a string into a list of substrings based on a separator   "hello world".split(" ")  # ["hello", "world"]
    string.join(iterable)           Joins a list of strings into a single string with a separator   " ".join(["hello", "world"])  # "hello world"
    string.lower()                   Converts all characters in a string to lowercase        "HELLO".lower()  # "hello"
    string.upper()                   Converts all characters in a string to uppercase        "hello".upper()  # "HELLO"
    string.strip()                   Removes whitespace from both ends     "  hello  ".strip()  # "hello"
    string.find(substring)          Returns the index of the first occurrence of a substring, or -1 if not found   "hello".find("e")  # 1
    substring in string              Checks if a substring exists within a string       "e" in "hello"  # True

    """