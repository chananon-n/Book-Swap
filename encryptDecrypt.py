from cryptography.fernet import Fernet
import os
import sys


class encryptDecrypt:
    def __init__(self):
        self.key = Fernet.generate_key()

    def writeKey(self):
        with open('filekey.key', 'wb') as filekey:
            filekey.write(self.key)

    def getKey(self):
        return self.key

    def encryptID(self):
        pass
        # TODO

    def decryptID(self):
        pass
        # TODO

    def encryptFile(self, file):
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
        with open(file, 'rb') as files:
            original = files.read()

        # encrypting the file
        encrypted = fernet.encrypt(original)

        # opening the file in write mode and
        # writing the encrypted data
        with open(file, 'wb') as encrypted_file:
            encrypted_file.write(encrypted)

    def decryptFile(self, file):
        # opening the key
        with open('filekey.key', 'rb') as filekey:
            key = filekey.read()
        # using the key
        fernet = Fernet(key)

        # opening the encrypted file
        with open(file, 'rb') as enc_file:
            encrypted = enc_file.read()

        # decrypting the file
        decrypted = fernet.decrypt(encrypted)

        # opening the file in write mode and
        # writing the decrypted data
        with open(file, 'wb') as dec_file:
            dec_file.write(decrypted)


if __name__ == "__main__":
    obj = encryptDecrypt()
    # obj.encryptFile()
    # obj.decryptFile()
