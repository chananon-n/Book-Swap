# create an abstract class Book
from abc import ABCMeta, abstractmethod
from library import BookType


class abstractBook(metaclass=ABCMeta):
    __metaclass__ = ABCMeta

    def __init__(self, picture, name, author, description, category, price):
        self.picture = picture
        self.name = name
        self.author = author
        self.description = description
        self.category = category
        self.price = price
        self.ID = 0

    def getBookID(self):
        return self.ID

    def get_price(self):
        return self.price

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

    @abstractmethod
    def setBookID(self,ID):
        self.ID = ID

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

    def to_json(self):
        # return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
        return {
            "picture": self.picture,
            "name": self.name,
            "author": self.author,
            "description": self.description,
            "category": self.category,
            "price": self.price,
        }



