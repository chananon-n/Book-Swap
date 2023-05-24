import asyncio

from tortoise import run_async
import CustomExeptionalHandler as CEH

import database


class storageSystem:
    def __init__(self):
        run_async(database.init())

    def createNewUser(self, name):
        try:
            run_async(database.databaseTools.create_id_name(name))
        except CEH.databaseException as e:
            return e.message + "Error in createNewUser"
        return True

    def getUserName(self, id):
        try:
            temp = asyncio.run(database.databaseTools.get_name(id))
            if temp is None:
                return "User not found"
            return temp
        except CEH.databaseException as e:
            return e.message + "Error in getUserName"

    def createNewBook(self, name):
        try:
            run_async(database.databaseTools.create_book_id_name(name))
        except CEH.databaseException as e:
            return e.message + "Error in createNewBook"
        return True

    def getBookName(self, id):
        try:
            temp = asyncio.run(database.databaseTools.get_book_name(id))
            if temp is None:
                return "Book not found"
            return temp
        except CEH.databaseException as e:
            return e.message + "Error in getBookName"

    def getBookID(self, name):
        try:
            temp = asyncio.run(database.databaseTools.get_book_id(name))
            if temp is None:
                return "Book not found"
            return temp
        except CEH.databaseException as e:
            return e.message + "Error in getBookID"

    def createBookStatus(self, book_id, user_id, status):
        try:
            run_async(database.databaseTools.create_book_status(book_id, user_id, status))
        except CEH.databaseException as e:
            return e.message + "Error in createBookStatus"
        return True

    def getBookStatus(self, book_id, user_id):
        try:
            temp = asyncio.run(database.databaseTools.get_book_status(book_id, user_id))
            if temp is None:
                return "Book status not found"
            return temp
        except CEH.databaseException as e:
            return e.message + "Error in getBookStatus"

    def removeBookStatus(self, book_id, user_id):
        try:
            return run_async(database.databaseTools.remove_book_status(book_id, user_id))
        except CEH.databaseException as e:
            return e.message + "Error in removeBookStatus"

    def getAvailableBooks(self, user_id):
        try:
            temp = asyncio.run(database.databaseTools.get_all_book("available", user_id))
            if temp is None:
                return "Book status not found"
            return temp
        except CEH.databaseException as e:
            return e.message + "Error in getAvailableBooks"

    def getBorrowedBooks(self, user_id):
        try:
            temp = asyncio.run(database.databaseTools.get_all_book("borrowed", user_id))
            if temp is None:
                return "Book status not found"
            return temp
        except CEH.databaseException as e:
            return e.message + "Error in getBorrowedBooks"

    def getAllBooks(self, user_id):
        try:
            temp = asyncio.run(database.databaseTools.get_all_book("all", user_id))
            if temp is None:
                return "Book status not found"
            return temp
        except CEH.databaseException as e:
            return e.message + "Error in getAllBooks"

    def checkStatusWithLocal(self, book_id, user_id, status):
        try:
            temp = asyncio.run(database.databaseTools.get_book_status(book_id, user_id))
            if temp is None:
                return "Book status not found"
            return temp == status
        except CEH.databaseException as e:
            return e.message + "Error in checkStatusWithLocal"
