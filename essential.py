import json
import random

from database import uploadToDB
from encryptDecrypt import encryptDecrypt


class essential:
    def __init__(self):
        self.key = encryptDecrypt()
        self.db = uploadToDB()

    def createNewID(self):
        randomId = random.randint(10000000, 99999999)
        while self.db.checkID(randomId):
            randomId = random.randint(10000000, 99999999)

        self.key.writeKey()

    def finishing(self):
        self.key.encryptFile("data.json")
        self.db.setFile('upload.json')
        self.db.uploadFile()

    def loggingIn(self, ID):
        # TODO check the encrypted ID with encrypted ID in database
        if self.db.checkID(ID):
            self.key.setKey(self.db.getKey(ID))
            self.db.downloadFile(ID)
            self.key.decryptFile("data.json")
        else:
            pass
            # TODO tell user that the ID is not in database

    def checkCredential(self):
        booksFromLocal = []
        booksFromDatabase = []

        with open('data.json') as file:
            rawdata = json.load(file)

        for key, value in rawdata.items():
            # print item in Book
            for key1, value1 in value['Book'].items():
                # get status of book
                status = value1['Status']
                # create dictionary of book contain book name and status
                book = {key1: status}
                # store all book in a list
                booksFromLocal.append(book)
                # print(booksFromLocal)

        with open('upload.json') as file:
            rawdata2 = json.load(file)

        for key, value in rawdata2['Book'].items():
            # print item in Book
            # get status of book
            status = value
            # create dictionary of book contain book name and status
            book = {key: status}
            # store all book in a list
            booksFromDatabase.append(book)
            # print(booksFromDatabase)

        return booksFromLocal != booksFromDatabase

    def updateLocalData(self):
        pass
        # TODO update local data with data from database
