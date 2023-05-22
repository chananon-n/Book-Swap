from datetime import datetime


class AddBook:
    def __init__(self, name, author):
        self.name = name
        self.author = author
        self.date = datetime.now()


class Module:
    def __init__(self):
        self.author = None
        self.name = None
        self.history = []

    def enrol(self):
        self.history.append(AddBook(self.name, self.author))

    def display(self):
        for i in self.history:
            print(i.name, i.author, i.date)
