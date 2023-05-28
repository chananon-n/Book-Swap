# create class eBook inherits from class Book
import random

from library.abstractBook import abstractBook


class eBook(abstractBook):
    def __init__(self, picture, name, author, description, category, price, pdf):
        super(eBook, self).__init__(picture, name, author, description, category, price)
        self.pdf = pdf
        self.ID = random.randint(10000, 100000)

    def get_pdf(self):
        return self.pdf

    def setBookID(self, ID):
        self.ID = ID

    def set_pdf(self, pdf):
        self.pdf = pdf

    @staticmethod
    def from_json(json):
        book = eBook(json['picture'], json['name'], json['author'], json['description'], json['category'],
                     json['price'])
        # book.set_pdf(json['pdf'])
        return book
