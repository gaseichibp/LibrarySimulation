import Person
import Book

class Library:
    def __init__(self):
        self.people = []
        self.books = []
        self.loans = []

    def registerPerson(self):
        name = input("Name: ")
        cpf = input("CPF: ")
        phone = input("Phone: ")
        p = Person.Person(name, cpf, phone)
        self.people.append(p)
        print("Person registered successfully!")

    def registerBook(self):
        category = input("Category: ")
        title = input("Title: ")
        author = input("Author: ")
        self.books.append(Book.Book(category, title, author))
        print("Book registered successfully!")

    def makeLoan(self):
        self.listPeople()
        personIndex = int(input("Person Index: "))
        if personIndex < len(self.people):
            self.listAvailableBooks()
            bookIndex = int(input("Book Index: "))
            if bookIndex < len(self.books):
                book = self.books[bookIndex]
                if book.available:
                    person = self.people[personIndex]
                    self.loans.append(Loan(person, book))
                    book.available = False
                    print("Loan made successfully!")
                else:
                    print("The book is already loaned.")
            else:
                print("Invalid book index!")
        else:
            print("Invalid person index!")

    def returnBook(self):
        self.listLoanedBooks()
        bookIndex = int(input("Index of the Book for Return: "))
        if bookIndex < len(self.books):
            book = self.books[bookIndex]
            if not book.available:
                book.available = True
                self.loans = [l for l in self.loans if l.book != book]
                print("Book returned successfully!")
            else:
                print("This book is already available.")
        else:
            print("Invalid book index!")

    def listPeople(self):
        for i, person in enumerate(self.people):
            print(f"{i}. {person}")

    def listBooks(self):
        for i, book in enumerate(self.books):
            print(f"{i}. {book}")

    def listAvailableBooks(self):
        print("=== Available Books ===")
        for i, book in enumerate(self.books):
            if book.available:
                print(f"{i}. {book}")

    def listLoanedBooks(self):
        print("=== Loaned Books ===")
        for loan in self.loans:
            print(loan)