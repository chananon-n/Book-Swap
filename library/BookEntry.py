class BookEntry:
    def __init__(self, t, name, author, price):
        self.type = t
        self.author = author
        self.price = price

    def __str__(self):
        return "Type: " + self.get_type() + "\nName: " + self.get_name() + "\nAuthor: " + self.get_author() + "\nPrice: " + str(
            self.get_price())

    def get_type(self):
        if self.type == 1:
            return "Book"
        elif self.type == 2:
            return "eBook"

    def get_name(self):
        return self.name

    def get_author(self):
        return self.author

    def get_price(self):
        if self.price >= 0:
            return self.price


class CreateBook:
    def __init__(self, entry):
        self.entry = entry

    def get_book(self):
        return self.entry
    
