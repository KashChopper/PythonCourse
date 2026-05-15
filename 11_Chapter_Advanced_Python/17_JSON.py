"""
JSON (JavaScript Object Notation) is a lightweight data interchange format that is easy for humans to read and write, and easy for machines to parse and generate. In Python, the json module is used to work with JSON data.
"""
import json
x = '{"Name":"Aasif", "age": 38}'

y = json.loads(x)

print(y["age"])