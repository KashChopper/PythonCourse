"""
Type hint are used to indicate the type of data that a variable is expected to hold. they don't affect the runtime behavior of the program.

"""
from typing import List, Tuple, Dict, Union



# Variable  Type Hinting
name: str = "Aasif"
age: int = 21


# Function Type Hinting 

def greet(name: str) -> str:
    return f"hello, {name}"

def sum(a: int, b: int) -> int:
    return a+b

# usage
print(greet("Aasif"))

print(sum(10,20))

print("________________________________Type Hinting with Collections________________________________")

numbers: List[int] = [1,2,4,5,6]
print(numbers)
# Tuple of a string and an integer

person: Tuple[str, int] = ('Aasif', 30)
print(person)

# Dictionary with string keys and integer values

scores: Dict[str, int] = {'Alice': 90, 'Bob': 85}
print(scores)
# Union type hinting
identifier: Union[int, str] = 12345
identifier = "Aasif12345"
print(identifier)