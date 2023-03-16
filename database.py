import firebase_admin
from firebase_admin import db
import json


class uploadToDB:
    def __init__(self):
        self.cred_obj = firebase_admin.credentials.Certificate('bookswap-9f0be-firebase-adminsdk-2wzkf-0550256fe0.json')
        self.default_app = firebase_admin.initialize_app(self.cred_obj, {
            'databaseURL': 'https://bookswap-9f0be-default-rtdb.asia-southeast1.firebasedatabase.app/'
        })
        self.ref = db.reference("/")
        self.file = ""

    def setFile(self, filename):
        self.file = filename

    def uploadFile(self):
        self.ref = db.reference("/")
        with open(self.file, "r") as f:
            file_contents = json.load(f)
        self.ref.update(file_contents)

    def downloadFile(self, ID):
        self.ref = db.reference("/" + str(ID))
        with open('upload.json', "w") as f:
            json.dump(self.ref.get(), f)

    def checkID(self, ID):
        self.ref = db.reference("/" + str(ID))
        if self.ref.get() is None:
            return False
        else:
            return True

    # get the key of the user
    def getKey(self, ID):
        self.ref = db.reference("/" + str(ID))
        return self.ref.get()["Key"]


# if __name__ == "__main__":
#     obj = uploadToDB()
#     obj.setFile('test.json')
#     obj.uploadFile()
    # obj.downloadFile("ID")
