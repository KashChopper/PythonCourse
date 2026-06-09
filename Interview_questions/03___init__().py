# What is __init__() in Python?

'''
__init__() is a special method in python also called as constructor which is automatically called when an object is created. It is used to initialize the attributes of the class. The __init__() method takes self as the first parameter which refers to the instance of the class and can take additional parameters to initialize the attributes.

'''

class book_shop:
    # constructor method
    def __init__(self, title):
        self.title = title

    # method to display the title of the book
    def display_title(self):
        print(f"The title of the book is {self.title}")

# creating an object of the book_shop class
book1 = book_shop("Rich Dad Poor Dad")
book1.display_title()