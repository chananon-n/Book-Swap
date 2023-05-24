import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QObject
from libraryUI.Home import Home
from libraryUI.Sign_in import Sign_in
from libraryUI.Sign_up import Sign_up
from library import Book
from library import eBook
import storageSystem

class librarySystem(QObject):
    # singleton
    __instance = None

    # constructor
    def __init__(self):
        # check if LibrarySystem is already created
        self.bookID = None
        self.s = storageSystem.storageSystem()
        self.book = Book.Book()
        self.eBook = eBook.eBook()
        if librarySystem.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            librarySystem.__instance = self
            self.__current = None

    def start(self):
        self.__current = Home()
        # Connect to the buttonClicked signal from the Home panel
        self.__current.buttonClicked.connect(self.handleButtonClicked)

    def handleButtonClicked(self, button_name):
        if button_name == "Sign_in":
            # Navigate to the Sign_in panel
            self.__current.close()
            sign_in = Sign_in()
            sign_in.signedIn.connect(self.backToHome)  # Main Menu
            self.__current = sign_in
        elif button_name == "Sign_up":
            # Navigate to the Sign_up panel
            self.__current.close()
            sign_up = Sign_up()
            sign_up.signedUp.connect(self.backToHome)  # Connect to the signedIn signal
            self.__current = Sign_up()

    def backToHome(self):
        self.__current.close()
        self.__current = Home()

    @staticmethod
    def get_instance():
        if librarySystem.__instance is None:
            librarySystem()
        return librarySystem.__instance

    @staticmethod
    def checkSignUp(self,name):
        if name == "" or name == "Enter the store name":
            return False
        else:
            self.s.createNewUser(name)
            return True

    def getUserID(self):
        pass

    def getUserName(self, user_id):
        return self.s.getUserName(user_id)

    def addNewBook(self, picture, name, author, description, category,price):
        book = Book.Book(picture, name, author, description, category)
        book.set_price(price)
        self.s.createNewBook(name)
        book.setBookID(self.s.getBookID(name))
        return book

    def addNewEbook(self, picture, name, author, description, category,price):
        ebook = eBook.eBook(picture, name, author, description, category)
        ebook.set_price(price)
        return ebook

    def getBookID(self, name):
        return self.s.getBookID(name)

    def createBookStatus(self, bookID, userID, status):
        self.s.createBookStatus(bookID, userID, status)
        return True

if __name__ == "__main__":
    app = QApplication([])
    library_system = librarySystem.get_instance()
    library_system.start()
    sys.exit(app.exec())
