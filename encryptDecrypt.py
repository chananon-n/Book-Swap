from cryptography.fernet import Fernet

import toJson
from database import uploadToDB


class encryptDecrypt:
    def __init__(self):
        self.key = Fernet.generate_key()

    # write the key to a file
    def writeKey(self):
        toJson.addDataBinary(self.key, 'filekey.key')

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
        key = toJson.readDataBinary('filekey.key')
        # string the key in a file
        toJson.addDataBinary(key, 'filekey.key')

        # opening the key
        key = toJson.readDataBinary('filekey.key')

        # using the generated key
        fernet = Fernet(key)

        # opening the original file to encrypt
        original = toJson.readDataBinary(file)

        # encrypting the file
        encrypted = fernet.encrypt(original)

        # opening the file in write mode and
        # writing the encrypted data
        toJson.addDataBinary(encrypted, file)

    # decrypt the file
    def decryptFile(self, file):
        # opening the key
        key = toJson.readDataBinary('filekey.key')
        # using the key
        fernet = Fernet(key)

        # opening the encrypted file
        encrypted = toJson.readDataBinary(file)

        # decrypting the file
        decrypted = fernet.decrypt(encrypted)

        # opening the file in write mode and
        # writing the decrypted data
        toJson.addDataBinary(decrypted, file)


if __name__ == "__main__":
    obj = encryptDecrypt()
    obj2 = uploadToDB()

    # obj.writeKey()
    # en = obj.encryptID(obj2, '12345678')
    # print(en)
    # de = obj.decryptID(obj2, en)
    # print(de)
    # obj.encryptFile('data.json')
    # obj.decryptFile('data.json')
