import json
import random

import toJson
from database import uploadToDB
from encryptDecrypt import encryptDecrypt


class essential:
    def __init__(self):
        self.key = encryptDecrypt()
        self.db = uploadToDB()

    def createNewID(self):
        randomId = random.randint(10000000, 99999999)
        encryptedID = self.key.encryptID(self.db, str(randomId))
        while self.db.checkID(encryptedID):
            randomId = random.randint(10000000, 99999999)
            encryptedID = self.key.encryptID(self.db, str(randomId))

        toJson.addData(encryptedID, 'upload.json')

        # TODO set user ID

    def finishing(self, data):
        self.key.encryptFile("data.json")
        # write the encrypted file to upload.json
        toJson.addData(data, 'upload.json')
        self.db.uploadFile()

    def loggingIn(self, ID):
        encryptedID = self.key.encryptID(self.db, ID)
        if self.db.checkID(encryptedID):
            self.key.setKey(self.db.getKey(ID))
            self.db.downloadFile(ID)
            self.key.decryptFile("data.json")
        else:
            pass
            # TODO tell user that the ID is not in database

    def checkCredential(self):
        booksFromLocal = []
        booksFromDatabase = []

        rawdata = toJson.loadData('data.json')

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

        rawdata2 = toJson.loadData('upload.json')

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


# if __name__ == "__main__":
    # obj = essential()
    # obj.createNewID()
