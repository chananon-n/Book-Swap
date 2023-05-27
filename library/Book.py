# create class Book inherits from class abstractBook
from datetime import datetime

from library.abstractBook import abstractBook


class Book(abstractBook):
    def __init__(self, picture, name, author, description, category, price):
        super(Book, self).__init__(picture, name, author, description, category, price)
        self.day = datetime.now()
        self.ID = 0
        self.status = "Available"

    def setStatus(self, status):
        self.status = status

    def setBookID(self, ID):
        self.ID = ID

    def get_day(self):
        return self.day

    def set_day(self, day):
        self.day = day

    def getStatus(self):
        return self.status

    def display(self):
        pass

    @staticmethod
    def from_json(json):
        book = Book(json['picture'], json['name'], json['author'], json['description'], json['category'], json['price'])
        return book
