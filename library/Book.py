# create class Book inherits from class abstractBook
from library import abstractBook
from datetime import datetime


class Book(abstractBook):
    def __init__(self, picture, name, author, description, category, price):
        super(Book, self).__init__(picture, name, author, description, category, price)
        self.day = datetime.now()
        self.ID = None
        self.status = True

    def setStatus(self, status):
        self.status = status

    def setBookID(self, ID):
        self.ID = ID

    def get_day(self):
        return self.day

    def get_price(self):
        return self.price*self.day.day

    def set_day(self, day):
        self.day = day

    def getBookID(self):
        return self.ID

    def display(self):
        pass
