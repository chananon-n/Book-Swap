# create an abstract class Book
from abc import ABCMeta, abstractmethod
from library import BookType


class abstractBook(metaclass=ABCMeta):
    __metaclass__ = ABCMeta

    def __init__(self, tp, picture, name, author, description, category, price):
        self.type = tp
        self.picture = picture
        self.name = name
        self.author = author
        self.description = description
        self.category = category
        self.price = price

    def get_price(self):
        return self.price

    def get_tyoe(self):
        return self.type

    def get_picture(self):
        return self.picture

    def get_title(self):
        return self.name

    def get_author(self):
        return self.author

    def get_description(self):
        return self.description

    def get_category(self):
        return self.category

    def set_picture(self, picture):
        self.picture = picture

    def set_title(self, title):
        self.name = title

    def set_author(self, author):
        self.author = author

    def set_description(self, description):
        self.description = description

    def set_category(self, category):
        self.category = category

    def set_price(self, price):
        self.price = price

    def __dict__(self):
        return {
            'picture': self.picture,
            'Name': self.name,
            'author': self.author,
            'description': self.description,
            'category': self.category
        }

    @abstractmethod
    def set_price(self, price):
        pass

    @abstractmethod
    def get_price(self):
        pass

    @abstractmethod
    def display(self):
        pass
