# Create a Book class that has two attributes:
#     title
#     author

# and two methods:
#     A method named .get_title() that returns: "Title: " + the instance title.
#     A method named .get_author() that returns: "Author: " + the instance author.

# and instantiate this class by creating 3 new books:
#     Pride and Prejudice - Jane Austen (PP)
#     Hamlet - William Shakespeare (H)
#     War and Peace - Leo Tolstoy (WP)

# The name of the new instances should be PP, H, and WP, respectively.
# For instance, if I instantiated the following book using this Book class:
#     Harry Potter - J.K. Rowling (HP)

# I would get the following attributes and methods:

class Book:
    def __init__(self, title: str, author: str) -> None:
        self.title = title
        self.author = author
    
    def get_title(self) -> str:
        return "Title: " + self.title
    
    def get_author(self) -> str:
        return "Author: " + self.author
    
PP = Book(title="Pride and Prejudice", author="Jane Austen")
H = Book(title="Hamlet", author="William Shakespeare")
WP = Book(title="War and Peace", author="Leo Tolstoy")
HP = Book(title="Harry Potter", author="J.K. Rowling")


