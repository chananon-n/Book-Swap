# create an abstract class Book
from abc import ABCMeta, abstractmethod


class Book(object):
    __metaclass__ = ABCMeta

    def __init__(self, picture, title, author, description, category, tags):
        self.picture = picture
        self.title = title
        self.author = author
        self.description = description
        self.category = category
        self.tags = tags

    def get_picture(self):
        return self.picture

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_description(self):
        return self.description

    def get_category(self):
        return self.category

    def get_tags(self):
        return self.tags

    def set_picture(self, picture):
        self.picture = picture

    def set_title(self, title):
        self.title = title

    def set_author(self, author):
        self.author = author

    def set_description(self, description):
        self.description = description

    def set_category(self, category):
        self.category = category

    def set_tags(self, tags):
        self.tags = tags

    @abstractmethod
    def set_price(self, price):
        pass

    @abstractmethod
    def get_price(self):
        pass

    @abstractmethod
    def display(self):
        pass
