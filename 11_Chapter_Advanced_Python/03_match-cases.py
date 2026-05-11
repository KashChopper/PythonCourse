"""
Introduced in Python 3.10,
match-case statements are a powerful feature in Python that allows you to perform pattern matching on data structures. They provide a more elegant and readable way to handle complex conditions compared to traditional if-elif-else statements.

#like switch case statement 
"""
def http_status(status):
    match status:
        case 200:
            print("OK")

        case 404:
            print("Not found")

        case 500:
            print("Internal server error")

        case _:
            print("Unknown status")

status = int(input("Enter the status code (200/ 404/ 500): "))
http_status(status)