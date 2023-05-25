import CustomExeptionalHandler as CEH

from database import databaseTools
from database import Tolocal
from database.databaseTools import *
from database.database_connection import init
from library.Book import Book
from library.eBook import eBook


class storageSystem:
    def __init__(self):
        pass

    @staticmethod
    def createNewUser(name):
        run_async(init())
        try:
            return asyncio.run(create_id_name(name))
        except CEH.databaseException as e:
            return e.message + "Error in createNewUser"

    @staticmethod
    def getUserName(id):
        run_async(init())
        try:
            return asyncio.run(get_name(id))
        except CEH.databaseException as e:
            return e.message + "Error in getUserName"

    @staticmethod
    def checkUserID(id):
        run_async(init())
        try:
            return asyncio.run(check_id(id))
        except CEH.databaseException as e:
            return e.message + "Error in checkUserID"

    @staticmethod
    def createNewBook(name):
        run_async(init())
        try:
            run_async(create_book_id_name(name))
            return True
        except CEH.databaseException as e:
            return e.message + "Error in createNewBook"
        return True

    @staticmethod
    def getBookName(id):
        run_async(init())
        try:
            return asyncio.run(get_book_name(id))
        except CEH.databaseException as e:
            return e.message + "Error in getBookName"

    @staticmethod
    def getBookID(name):
        run_async(init())
        try:
            return asyncio.run(get_book_id(name))
        except CEH.databaseException as e:
            return e.message + "Error in getBookID"

    @staticmethod
    def createBookStatus(book_id, user_id, status):
        run_async(init())
        try:
            run_async(databaseTools.create_book_status(book_id, user_id, status))
            return True
        except CEH.databaseException as e:
            return e.message + "Error in createBookStatus"

    @staticmethod
    def getBookStatus(book_id, user_id):
        run_async(init())
        try:
            return asyncio.run(get_book_status(book_id, user_id))
        except CEH.databaseException as e:
            return e.message + "Error in getBookStatus"

    @staticmethod
    def removeBookStatus(book_id, user_id):
        run_async(init())
        try:
            return asyncio.run(remove_book_status(book_id, user_id))
        except CEH.databaseException as e:
            return e.message + "Error in removeBookStatus"

    @staticmethod
    def getAvailableBooks(user_id):
        run_async(init())
        try:
            return asyncio.run(get_all_book("available", user_id))
        except CEH.databaseException as e:
            return e.message + "Error in getAvailableBooks"

    @staticmethod
    def getBorrowedBooks(user_id):
        run_async(init())
        try:
            return asyncio.run(databaseTools.get_all_book("borrowed", user_id))
        except CEH.databaseException as e:
            return e.message + "Error in getBorrowedBooks"

    @staticmethod
    def getAllBooks(user_id):
        run_async(init())
        try:
            return asyncio.run(get_all_book("all", user_id))
        except CEH.databaseException as e:
            return e.message + "Error in getAllBooks"

    @staticmethod
    def checkStatusWithLocal(book_id, user_id, status):
        run_async(init())
        try:
            temp = asyncio.run(databaseTools.get_book_status(book_id, user_id))
            return temp == status
        except CEH.databaseException as e:
            return e.message + "Error in checkStatusWithLocal"

    @staticmethod
    def editBookName(book_id, name):
        run_async(init())
        try:
            return asyncio.run(databaseTools.edit_book_name(book_id, name))
        except CEH.databaseException as e:
            return e.message + "Error in editBookName"

    @staticmethod
    def getBooksFromLocal():
        books = Tolocal.load_book_from_resource()
        result = []
        # get type of books
        for i in range(len(books)):
            if type(books[i]) == Book:
                result.append(books[i])
        return result

    @staticmethod
    def getEBooksFromLocal():
        books = Tolocal.load_book_from_resource()
        result = []
        # get type of books
        for i in range(len(books)):
            if type(books[i]) == eBook:
                result.append(books[i])
        return result

    @staticmethod
    def saveToLocal(books):
        Tolocal.save_book_to_resource(books)
        return True


# print(storageSystem.checkUserID(6))
# run_async(init())
# a = asyncio.run(check_id(659))
# print(a)
