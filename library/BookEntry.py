import BookType

from library import abstractBook
from library import BookType
class BookEntry(abstractBook):
    def __init__(self, picture, title, author, description, category):
        super(BookEntry, self).__init__(picture, title, author, description, category)
        self.price = 0.0
        self.type = None

    def __str__(self):
        return "Type: " + self.get_type() + "\nName: " + self.get_name() + "\nAuthor: " + self.get_author() + "\nPrice: " + str(
            self.get_price())

    def get_type(self):
        if self.type == BookType.BookType(1):
            return "Book"
        elif self.type == BookType.BookType(2):
            return "eBook"

    def get_name(self):
        return self.name

    def get_author(self):
        return self.author

    def get_price(self):
        if self.price >= 0:
            return self.price


class CreateBook:
    def __init__(self, entry):
        self.entry = entry

    def get_book(self):
        return self.entry
