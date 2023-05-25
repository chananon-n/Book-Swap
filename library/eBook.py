# create class eBook inherits from class Book
import random

from library.abstractBook import abstractBook


class eBook(abstractBook):
    def __init__(self, picture, name, author, description, category, price):
        super(eBook, self).__init__(picture, name, author, description, category, price)
        self.pdf = ""
        self.ID = random.randint(10000, 100000)

    def getPdf(self):
        return self.pdf

    def get_ID(self):
        return self.ID

    def get_pdf(self):
        return self.pdf

    def set_pdf(self, pdf):
        self.pdf = pdf

    def set_price(self, price):
        self.price = price

    def setPDF(self, pdf):
        self.pdf = pdf

    def get_price(self):
        return self.price

    def display(self):
        pass
