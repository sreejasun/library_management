class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.checked_out = False

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)

    def display_books(self):
        for index, book in enumerate(self.books, start=1):
            status = "Available" if not book.checked_out else "Checked Out"
            print(f"{index}. {book.title} by {book.author} ({status})")

    def checkout_book(self, book_index):
        if 1 <= book_index <= len(self.books):
            book = self.books[book_index - 1]
            if not book.checked_out:
                book.checked_out = True
                print(f"{book.title} has been checked out.")
            else:
                print(f"{book.title} is already checked out.")
        else:
            print("Invalid book index.")

    def return_book(self, book_index):
        if 1 <= book_index <= len(self.books):
            book = self.books[book_index - 1]
            if book.checked_out:
                book.checked_out = False
                print(f"{book.title} has been returned.")
            else:
                print(f"{book.title} is not checked out.")
        else:
            print("Invalid book index.")

def main():
    lib= Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add a book")
        print("2. Display books")
        print("3. Check out a book")
        print("4. Return a book")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter the title of the book: ")
            author = input("Enter the author of the book: ")
            lib.add_book(title, author)
            print("Book added successfully.")
        elif choice == "2":
            lib.display_books()
        elif choice == "3":
            lib.display_books()
            book_index = int(input("Enter the index of the book to check out: "))
            lib.checkout_book(book_index)
        elif choice == "4":
            lib.display_books()
            book_index = int(input("Enter the index of the book to return: "))
            lib.return_book(book_index)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()