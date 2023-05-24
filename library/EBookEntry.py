from library import abstractBook
from library import BookType


class EBookEntry(abstractBook):
    def __init__(self, picture, title, author, description, category):
        super(EBookEntry, self).__init__(picture, title, author, description, category)
        self.price = 0.0
        self.type = None
        self.pdf = ""

    def get_price(self):
        return self.price

    def get_type(self):
        if self.type == BookType.BookType(1):
            return "Book"
        elif self.type == BookType.BookType(2):
            return "eBook"

    def get_pdf(self):
        return self.pdf

    def set_price(self, price):
        self.price = price

    def set_pdf(self, pdf):
        self.pdf = pdf


class createEbook:
    def __init__(self, entry):
        self.entry = entry

    def get_ebook(self):
        return self.entry
