import Person
import Book

class Loan:
    def __init__(self, person, book):
        self._person = person
        self._book = book

    @property
    def person(self):
        return self._person

    @property
    def book(self):
        return self._book

    def __str__(self):
        return f"Loan{{person={self.person.name}, book={self.book.title}}}"