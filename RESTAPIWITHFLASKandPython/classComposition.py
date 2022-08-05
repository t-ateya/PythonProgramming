class BookShelf:
    def __init__(self, *books):
        self.books = books 

    def __str__(self) -> str:
        return f"Bookshelf with {len(self.books)} books."


class Book:
    def __init__(self, name):
        self.name = name 

    def __str__(self):
        return f"Book {self.name}"

    

b1 = Book("Harry Potter")
b2 = Book("Great Programmer")
b3 = Book("In love with my bestie")

bs = BookShelf(b1, b2,b3)
print(bs)