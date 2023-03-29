import firebase_admin
from firebase_admin import db
import json

import toJson


class uploadToDB:
    def __init__(self):
        self.cred_obj = firebase_admin.credentials.Certificate('bookswap-9f0be-firebase-adminsdk-2wzkf-0550256fe0.json')
        self.default_app = firebase_admin.initialize_app(self.cred_obj, {
            'databaseURL': 'https://bookswap-9f0be-default-rtdb.asia-southeast1.firebasedatabase.app/'
        })
        self.ref = db.reference("/")
        self.file = ""

    # set the file to upload
    def setFile(self, filename):
        self.file = filename

    # upload the file to database
    def uploadFile(self):
        self.ref = db.reference("/")
        file_contents = toJson.loadData(self.file)
        self.ref.update(file_contents)

    # download the file from database
    def downloadFile(self, ID):
        self.ref = db.reference("/" + str(ID))
        toJson.addData(self.ref.get(), "upload.json", 'w')

    # check if the ID is in database
    def checkID(self, ID):
        self.ref = db.reference("/" + str(ID))
        if self.ref.get() is None:
            return False
        else:
            return True

    # get the key of the ID
    def getKey(self, ID):
        self.ref = db.reference("/" + str(ID))
        return self.ref.get()["Key"]

    # get the universal key that is used to encrypt the ID
    def getUniKey(self):
        self.ref = db.reference("/Universal Key")
        return self.ref.get()


# if __name__ == "__main__":
#     obj = uploadToDB()
#     obj.setFile('test.json')
#     obj.uploadFile()
#     obj.downloadFile("ID")
