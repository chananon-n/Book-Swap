# create class Book inherits from class abstractBook
from library import abstractBook
from datetime import datetime


class Book(abstractBook):
    def __init__(self, picture, name, author, description, category, tags):
        super(Book, self).__init__(picture, name, author, description, category, tags)
        self.price = 0.0
        self.day = datetime.now()
        self.status = True

    def setStatus(self, status):
        self.status = status

    def get_day(self):
        return self.day

    def set_day(self, day):
        self.day = day

    def set_price(self, price):
        self.price = price * self.day

    def get_price(self):
        return self.price

    def display(self):
        pass
