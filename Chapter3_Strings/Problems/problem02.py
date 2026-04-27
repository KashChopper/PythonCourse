"""
Write a program to fill in a letter template given below with name and date.
letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''
"""

letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''

print(letter.replace("<|Name|>", "Aasif").replace("<|Date|>", "01,01,2022"))


name = "Aasif"
date = "1/1/2001"

print(f"""
Dear {name},
You are selected!
{date}

""")
