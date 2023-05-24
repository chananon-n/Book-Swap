# create class eBook inherits from class Book
import random

from library import abstractBook


class eBook(abstractBook):
    def __init__(self,picture, name, author, description, category):
        super(eBook, self).__init__(picture, name, author, description, category)
        self.price = 0.0
        self.pdf = None
        self.ID = None

    def get_ID(self):
        return self.ID

    def get_pdf(self):
        return self.pdf

    def set_pdf(self, pdf):
        self.pdf = pdf

    def set_price(self, price):
        self.price = price

    def get_price(self):
        return self.price

    def createEbookID(self):
        self.ID = random.randint(10000, 100000)

    def display(self):
        pass
