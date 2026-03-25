# library_test.py

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_checked_out = False

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        """Adds a book to the library."""
        self.books.append(book)

    def find_book_by_isbn(self, isbn):
        # SMELL: Inefficient linear search for large datasets
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def checkout_book(self, isbn):
        book = self.find_book_by_isbn(isbn)
        
        # BUG: This will crash if book is None (AttributeError)
        # CodeRabbit should suggest a null check here.
        if book.is_checked_out:
            print(f"Error: {book.title} is already checked out.")
            return False
        
        book.is_checked_out = True
        return True

    def get_all_titles(self):
        # SMELL: Unnecessary list comprehension/performance
        titles = []
        for i in range(len(self.books)):
            titles.append(self.books[i].title)
        return titles

# --- Test Execution ---
if __name__ == "__main__":
    my_library = Library()
    my_library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald", "12345"))
    my_library.add_book(Book("1984", "George Orwell", "67890"))

    # This works
    print(f"Titles: {my_library.get_all_titles()}")
    
    # This will trigger the bug if you uncomment it
    # my_library.checkout_book("99999")
