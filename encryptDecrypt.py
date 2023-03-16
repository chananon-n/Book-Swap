from cryptography.fernet import Fernet
import os
import sys


class encryptDecrypt:
    def __init__(self):
        self.key = ""

    def getKey(self):
        pass
        # TODO get the key from database

    def encryptID(self):
        pass
        # TODO

    def decryptID(self):
        pass
        # TODO

    def encryptFile(self):
        # opening the key
        with open('filekey.key', 'rb') as filekey:
            key = filekey.read()

        # string the key in a file
        with open('filekey.key', 'wb') as filekey:
            filekey.write(key)

        # opening the key
        with open('filekey.key', 'rb') as filekey:
            key = filekey.read()

        # using the generated key
        fernet = Fernet(key)

        # opening the original file to encrypt
        with open('test.json', 'rb') as file:
            original = file.read()

        # encrypting the file
        encrypted = fernet.encrypt(original)

        # opening the file in write mode and
        # writing the encrypted data
        with open('test.json', 'wb') as encrypted_file:
            encrypted_file.write(encrypted)

    def decryptFile(self):
        # opening the key
        with open('filekey.key', 'rb') as filekey:
            key = filekey.read()
        # using the key
        fernet = Fernet(key)

        # opening the encrypted file
        with open('test.json', 'rb') as enc_file:
            encrypted = enc_file.read()

        # decrypting the file
        decrypted = fernet.decrypt(encrypted)

        # opening the file in write mode and
        # writing the decrypted data
        with open('test.json', 'wb') as dec_file:
            dec_file.write(decrypted)


if __name__ == "__main__":
    obj = encryptDecrypt()
    # obj.encryptFile()
    # obj.decryptFile()
