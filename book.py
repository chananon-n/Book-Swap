# create class Book inherits from class abstractBook
import abstractBook


class Book(abstractBook.Book):
    def __init__(self, picture, title, author, description, category, tags):
        super(Book, self).__init__(picture, title, author, description, category, tags)
        self.price = 0.0
        self.day = 0

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