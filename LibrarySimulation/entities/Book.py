class Book:
    def __init__(self, category, title, author):
        self._category = category
        self._title = title
        self._author = author
        self._available = True

    @property
    def category(self):
        return self._category

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def available(self):
        return self._available

    @available.setter
    def available(self, value):
        self._available = value

    def __str__(self):
        return f"Book{{category='{self._category}', title='{self._title}', author='{self._author}', available={self._available}}}"