from cryptography.fernet import Fernet
from database import uploadToDB


class encryptDecrypt:
    def __init__(self):
        self.key = Fernet.generate_key()

    # write the key to a file
    def writeKey(self):
        with open('filekey.key', 'wb') as filekey:
            filekey.write(self.key)

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

    # decrypt the file
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
    obj2 = uploadToDB()


    # obj.encryptFile()
    # obj.decryptFile()
