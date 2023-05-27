from datetime import datetime


class AddBook:
    def __init__(self, t, name, author):
        self.type = t
        self.name = name
        self.author = author
        self.date = datetime.now()



