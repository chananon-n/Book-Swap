from cryptography.fernet import Fernet

import toJson
from database import uploadToDB


class encryptDecrypt:
    def __init__(self):
        self.key = Fernet.generate_key()

    # write the key to a file
    def writeKey(self):
        toJson.addData(self.key, 'filekey.key', 'wb')

    # set the key from the key file
    def setKey(self, key):
        self.key = key

    # get the key
    def getKey(self):
        return self.key

    # encrypt the ID
    def encryptID(self, key, id):
        fernet = Fernet(bytes(key.getUniKey(), 'utf-8'))
        return fernet.encrypt(bytes(id, 'utf-8'))

    # decrypt the ID
    def decryptID(self, key, id):
        fernet = Fernet(bytes(key.getUniKey(), 'utf-8'))
        return fernet.decrypt(id).decode('utf-8')

    # encrypt the file
    def encryptFile(self, file):
        # opening the key
        key = toJson.readData('filekey.key', 'rb')
        # string the key in a file
        toJson.addData(key, 'filekey.key', 'wb')

        # opening the key
        key = toJson.readData('filekey.key', 'rb')

        # using the generated key
        fernet = Fernet(key)

        # opening the original file to encrypt
        original = toJson.readData(file, 'rb')

        # encrypting the file
        encrypted = fernet.encrypt(original)

        # opening the file in write mode and
        # writing the encrypted data
        toJson.addData(encrypted, file, 'wb')

    # decrypt the file
    def decryptFile(self, file):
        # opening the key
        key = toJson.readData('filekey.key', 'rb')
        # using the key
        fernet = Fernet(key)

        # opening the encrypted file
        encrypted = toJson.readData(file, 'rb')

        # decrypting the file
        decrypted = fernet.decrypt(encrypted)

        # opening the file in write mode and
        # writing the decrypted data
        toJson.addData(decrypted, file, 'wb')


if __name__ == "__main__":
    obj = encryptDecrypt()
    obj2 = uploadToDB()


    # obj.encryptFile()
    # obj.decryptFile()
