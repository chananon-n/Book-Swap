import os
import sys
from PySide6.QtWidgets import QApplication

import libraryUI.Add_book
from library import Book
from library import eBook
from library import AddBook
from libraryUI.Home import Home
import libraryUI.Sign_in as Sign_in
import libraryUI.Main_menu as Main_menu
import libraryUI.Sign_up as Sign_up
import libraryUI.Add_book as Add_book
import libraryUI.remove_book as remove_book
import libraryUI.editBook as editBook


class librarySystem:
    # singleton
    history_list = []
    ebook_list = []
    book_list = []
    __instance = None
    state = None
    userID = None
    select = None

    # constructor
    def __init__(self):
        # check if LibrarySystem is already created
        super().__init__()
        if librarySystem.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            librarySystem.__instance = self
            self.__current = None

    def start(self):
        librarySystem.state = "Home"
        librarySystem.__current = Home()

    @staticmethod
    def setState(state):
        librarySystem.state = state
        librarySystem.checkState()

    @staticmethod
    def checkState():
        if librarySystem.state == "Home":
            librarySystem.__current = Home()
        if librarySystem.state == "Sign_in":
            librarySystem.__current = Sign_in.Sign_in()
        if librarySystem.state == "Sign_up":
            librarySystem.__current = Sign_up.Sign_up()
        if librarySystem.state == "Main_menu":
            librarySystem.__current = Main_menu.Main_menu()
        if librarySystem.state == "Add_book":
            librarySystem.__current = Add_book.Add_book()
        if librarySystem.state == "Edit_book":
            librarySystem.__current = remove_book.Remove_Book()
        if librarySystem.state == "Edit_Ebook":
            librarySystem.__current = editBook.EditEbook()

    @staticmethod
    def get_instance():
        if librarySystem.__instance is None:
            librarySystem()
        return librarySystem.__instance

    @staticmethod
    def setUserSelect(select):
        librarySystem.select = select

    @staticmethod
    def getUserSelect():
        return librarySystem.select

    @staticmethod
    def CheckUserID(userID):
        from storageSystem import storageSystem
        if storageSystem.checkUserID(userID):
            librarySystem.__userID = userID
            return True
        return False

    @staticmethod
    def setUserID(userID):
        librarySystem.userID = userID

    @staticmethod
    def getUserID():
        return librarySystem.userID

    @staticmethod
    def getUserName(user_id):
        from storageSystem import storageSystem
        return storageSystem.getUserName(user_id)

    @staticmethod
    def addNewBook(picture, name, author, description, category, price):
        book = Book.Book(picture, name, author, description, category, price)
        from storageSystem import storageSystem
        try:
            bookId = storageSystem.createNewBook(name)
        except RuntimeError:
            bookId = storageSystem.createNewBook(name)
        try:
            storageSystem.createBookStatus(bookId, librarySystem.getUserID(), 1)
        except RuntimeError:
            storageSystem.createBookStatus(bookId, librarySystem.getUserID(), 1)
        book.setBookID(bookId)
        librarySystem.book_list.append(book)
        history = AddBook.AddBook(1, name, author)
        librarySystem.history_list.append(history)
        return book

    @staticmethod
    def getHistory():
        return librarySystem.history_list

    @staticmethod
    def addNewEbook(picture, name, author, description, category, price, pdf):
        ebook = eBook.eBook(picture, name, author, description, category, price, pdf)
        librarySystem.ebook_list.append(ebook)
        history = AddBook.AddBook(2, name, author)
        librarySystem.history_list.append(history)
        return ebook

    @staticmethod
    def searchBook(name):
        search_result = []
        for book in librarySystem.book_list:
            if name in book.get_name():
                search_result.append(book)
        return search_result

    @staticmethod
    def searchEbook(name):
        search_result = []
        for ebook in librarySystem.ebook_list:
            if name in ebook.get_title():
                search_result.append(ebook)
        return search_result

    @staticmethod
    def createUserID(name):
        from storageSystem import storageSystem
        return storageSystem.createNewUser(name)

    def filterCategory(category):
        bookList = []
        allBook = librarySystem.book_list
        for book in allBook:
            if (book.get_category() == category) and (book not in bookList):
                bookList.append(book)
        return bookList

    @staticmethod
    def filterCategoryEbook(category):
        ebookList = []
        allEbook = librarySystem.ebook_list
        for ebook in allEbook:
            if (ebook.get_category() == category) and (ebook not in ebookList):
                ebookList.append(ebook)
        return ebookList

    @staticmethod
    def createBookStatus(bookID, userID, status):
        from storageSystem import storageSystem
        storageSystem.createBookStatus(bookID, userID, status)
        return True

    @staticmethod
    def getBookStatus(bookID, userID):
        from storageSystem import storageSystem
        return storageSystem.getBookStatus(bookID, userID)

    @staticmethod
    def removeBookStatus(bookID, userID):
        from storageSystem import storageSystem
        storageSystem.removeBookStatus(bookID, userID)
        return True

    @staticmethod
    def getBookAvailable(userID):
        from storageSystem import storageSystem
        return storageSystem.getAvailableBooks(userID)

    @staticmethod
    def getBorrowList(userID):
        from storageSystem import storageSystem
        return storageSystem.getBorrowedBooks(userID)

    @staticmethod
    def getBookListFromDB(userID):
        from storageSystem import storageSystem
        return storageSystem.getAllBooks(userID)

    @staticmethod
    def getEBookListFromLocal():
        from storageSystem import storageSystem
        return storageSystem.getEBooksFromLocal()

    @staticmethod
    def getBookListFromLocal():
        from storageSystem import storageSystem
        return storageSystem.getBooksFromLocal()

    @staticmethod
    def getAllBooks():
        return librarySystem.book_list

    @staticmethod
    def getAllEbook():
        return librarySystem.ebook_list

    @staticmethod
    def checkStatus(bookID, userID, status):
        from storageSystem import storageSystem
        return storageSystem.checkStatusWithLocal(bookID, userID, status)

    @staticmethod
    def editBook(b: Book, bookID, name, author, description, category, price):
        from storageSystem import storageSystem
        storageSystem.editBookName(bookID, name)
        b.setName(name)
        b.setauthor(author)
        b.setdescription(description)
        b.setcategory(category)
        b.setPrice(price)
        return True

    @staticmethod
    def removeBook(b: Book, bookID, userID):
        from storageSystem import storageSystem
        storageSystem.removeBookStatus(bookID, userID)
        b.deleteBook()
        return True

    @staticmethod
    def removeEBook(e: eBook):
        # delete ebook from local
        e.deleteEBook()
        return True

    @staticmethod
    def editEbook(e: eBook, name, author, description, category, price, pdf):
        e.setName(name)
        e.setauthor(author)
        e.setdescription(description)
        e.eBook.setcategory(category)
        e.eBook.set_price(price)
        e.eBook.set_pdf(pdf)
        return True

    @staticmethod
    def finishAndSave():
        from storageSystem import storageSystem
        for i in librarySystem.book_list:
            storageSystem.saveToLocal(i)
        for j in librarySystem.ebook_list:
            storageSystem.saveToLocal(j)
        return True

    @staticmethod
    def save_images(pixmap, title_name):
        # create BookSwap resources/images folder if not exist
        image_dir = os.path.join(os.path.dirname(__file__), 'BookSwap resources/images')
        if not os.path.exists(image_dir):
            os.makedirs(image_dir)
        if title_name and pixmap:
            sanitized_title = ''.join(c for c in title_name if c.isalnum() or c in ['-', '_'])
            image_path = os.path.join(image_dir, sanitized_title + '.png')
            pixmap.save(image_path, 'PNG')
            return True
        else:
            return False


# librarySystem.book_list = librarySystem.getBookListFromLocal()
# librarySystem.ebook_list = librarySystem.getEBookListFromLocal()
# print(librarySystem.book_list)
# print(librarySystem.ebook_list)
# print(storageSystem.getBookID("test"))
# storageSystem.createNewBook("test2")

if __name__ == "__main__":
    app = QApplication([])
    library_system = librarySystem.get_instance()
    library_system.start()
    sys.exit(app.exec())

