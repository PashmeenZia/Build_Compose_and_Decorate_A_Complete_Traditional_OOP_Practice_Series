class Book:
    total_books = 0  # class variable

    def __init__(self, title):
        self.title = title
        Book.increment_book_count()

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

    @classmethod
    def show_total_books(cls):
        print("Total books added:", cls.total_books)

# Objects create karte hain
b1 = Book("Python Basics")
b2 = Book("AI for Beginners")

# Show total books using class method
Book.show_total_books()
