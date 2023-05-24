from datetime import datetime


class AddBook:
    def __init__(self, type, name, author):
        self.type = type
        self.name = name
        self.author = author
        self.date = datetime.now()


class Module:
    def __init__(self):
        self.author = None
        self.name = None
        self.history = []

    def add_history(self,a: AddBook):
        self.history.append(a)

    def display(self):
        for i in self.history:
            print(i.name, i.author, i.date)
