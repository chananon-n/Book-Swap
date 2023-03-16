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
        self.ref.set(file_contents)

    def downloadFile(self, ID):
        self.ref = db.reference("/" + ID)
        with open(self.file, "w") as f:
            json.dump(self.ref.get(), f)


# if __name__ == "__main__":
#     obj = uploadToDB()
#     obj.setFile('test.json')
#     obj.uploadFile()
    # obj.downloadFile("ID")
