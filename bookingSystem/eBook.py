# create class eBook inherits from class Book
from bookingSystem import abstractBook


class eBook(abstractBook):
    def __init__(self, picture, title, author, description, category, tags):
        super(eBook, self).__init__(picture, title, author, description, category, tags)
        self.price = 0.0
        self.pdf = None

    def get_pdf(self):
        return self.pdf

    def set_pdf(self, pdf):
        self.pdf = pdf

    def set_price(self, price):
        self.price = price

    def get_price(self):
        return self.price

    def display(self):
        pass
