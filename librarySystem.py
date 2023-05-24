import os
import sys
from PySide6.QtWidgets import QApplication
from library import Book
from library import eBook
import storageSystem
from libraryUI.Home import Home
from library import AddBook


class librarySystem:
    # singleton
    __instance = None

    # constructor
    def __init__(self):
        # check if LibrarySystem is already created
        super().__init__()
        self.userID = None
        self.s = storageSystem.storageSystem()
        if librarySystem.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            librarySystem.__instance = self
            self.__current = None
        self.book_list = []
        self.ebook_list = []
        self.history_list = []

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
    def checkSignUp(self, name):
        if name == "" or name == "Enter the store name":
            return False
        else:
            self.s.createNewUser(name)
            return True

    def CheckUserID(self, id):
        self.userID = id
        return self.s.checkUserID(id)

    def getUserName(self, user_id):
        return self.s.getUserName(user_id)

    def addNewBook(self, picture, name, author, description, category, price):
        book = Book.Book(picture, name, author, description, category, price)
        self.s.createNewBook(name)
        book.setBookID(self.s.getBookID(name))
        self.book_list.append(book)
        history = AddBook.AddBook(1, name, author)
        self.history_list.append(history)
        return book

    def addNewEbook(self, picture, name, author, description, category, price):
        ebook = eBook.eBook(picture, name, author, description, category, price)
        self.ebook_list.append(ebook)
        history = AddBook.AddBook(2, name, author)
        self.history_list.append(history)
        return ebook

    def getBookID(self, name):
        return self.s.getBookID(name)

    def searchBook(self, name):
        search_result = []
        for book in self.book_list:
            if name in book.get_name():
                search_result.append(book)
        return search_result

    def searchEbook(self, name):
        search_result = []
        for ebook in self.ebook_list:
            if name in ebook.get_name():
                search_result.append(ebook)
        return search_result

    def filterCategory(self, category):
        bookList = []
        allBook = self.s.getAllBooks(self.userID)
        for book in allBook:
            if (book.get_category() == category) and (book not in bookList):
                bookList.append(book)
        return bookList

    def createBookStatus(self, bookID, userID, status):
        self.s.createBookStatus(bookID, userID, status)
        return True

    def getBookStatus(self, bookID, userID):
        return self.s.getBookStatus(bookID, userID)

    def removeBookStatus(self, bookID, userID):
        self.s.removeBookStatus(bookID, userID)
        return True

    def getBookAvailable(self, userID):
        return self.s.getAvailableBooks(userID)

    def getBorrowList(self, userID):
        return self.s.getBorrowedBooks(userID)

    def getBookListFromDB(self, userID):
        return self.s.getAllBooks(userID)

    def getEBookListFromLocal(self):
        return self.s.getEBooksFromLocal()

    def getBookListFromLocal(self):
        return self.s.getBooksFromLocal()

    def checkStatus(self, bookID, userID, status):
        return self.s.checkStatusWithLocal(bookID, userID, status)

    def editBook(self, b: Book, bookID, name, author, description, category, price):
        self.s.editBookName(bookID, name)
        b.setName(name)
        b.setauthor(author)
        b.setdescription(description)
        b.setcategory(category)
        b.set_price(price)
        return True

    def removeBook(self, b: Book, bookID, userID):
        self.s.removeBookStatus(bookID, userID)
        del b
        return True

    @staticmethod
    def removeEBook(self, e: eBook):
        del e
        return True

    @staticmethod
    def editEbook(self, e: eBook, name, author, description, category, price):
        e.setName(name)
        e.setauthor(author)
        e.setdescription(description)
        e.eBook.setcategory(category)
        e.eBook.set_price(price)
        return True

    def finishAndSave(self):
        book = self.getBookListFromDB(self.userID)
        bookLocal = self.getBookListFromLocal()
        if book == bookLocal:
            return self.s.saveToLocal(self.book)
        return False

    @staticmethod
    def save_images(pixmap, title_name):
        # create BookSwap resources/images folder if not exist
        image_dir = os.path.join(os.path.dirname(__file__), 'BookSwap resources/images')
        if not os.path.exists(image_dir):
            os.makedirs(image_dir)
        if title_name is not None:
            image_path = os.path.join(image_dir, title_name + '.jpg')
            pixmap.save(image_path, 'jpg')
            return True
        else:
            return False


if __name__ == "__main__":
    app = QApplication([])
    library_system = librarySystem.get_instance()
    library_system.start()
    sys.exit(app.exec())

