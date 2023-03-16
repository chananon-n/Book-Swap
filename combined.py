import random
from Book import Book
from database import uploadToDB
from eBook import eBook
from encryptDecrypt import encryptDecrypt
from toJson import toJson

if __name__ == "__main__":
    # # if create new ID
    # # generate random integer 8 digits using random
    # toDatabase = uploadToDB()
    # randomId = random.randint(10000000, 99999999)
    # while toDatabase.checkID(randomId):
    #     randomId = random.randint(10000000, 99999999)
    #
    # keyCredential = encryptDecrypt()
    # keyCredential.writeKey()
    #
    # # data to upload to database
    # datas1 = {randomId: {'Key': keyCredential.getKey().__str__(), 'Book': {'Book1': 0, 'Book2': 1, 'Book3': 1},
    #                      'E-Book': {'eBook1': 0, 'eBook2': 1, 'eBook3': 1}
    #                      }}
    #
    # update = toJson()
    # update.setData(datas1)
    # update.addData("upload.json")
    #
    # # data to write and encrypt to file in local
    # book1 = Book("Book1", "Author1", "Publisher1", "ISBN1", "Description1", "Category1")
    # book2 = Book("Book2", "Author2", "Publisher2", "ISBN2", "Description2", "Category2")
    # book3 = Book("Book3", "Author3", "Publisher3", "ISBN3", "Description3", "Category3")
    # ebook1 = eBook("eBook1", "Author1", "Publisher1", "ISBN1", "Description1", "Category1")
    # ebook2 = eBook("eBook2", "Author2", "Publisher2", "ISBN2", "Description2", "Category2")
    # ebook3 = eBook("eBook3", "Author3", "Publisher3", "ISBN3", "Description3", "Category3")
    #
    # datas2 = {'ID': {'Book store name': 'Book store 1',
    #                  'Book': {'Book1': {'Title': book1.title, 'Author': book1.author},
    #                           'Book2': {'Title': book2.title, 'Author': book2.author},
    #                           'Book3': {'Title': book3.title, 'Author': book3.author}},
    #                  'eBook': {'eBook1': {'Title': ebook1.title, 'Author': ebook1.author},
    #                            'eBook2': {'Title': ebook2.title, 'Author': ebook2.author},
    #                            'eBook3': {'Title': ebook3.title, 'Author': ebook3.author}}
    #                  }
    #           }
    #
    # update = toJson()
    # update.setData(datas2)
    # update.addData("data.json")
    #
    # # encrypt file
    # keyCredential.encryptFile("data.json")
    #
    # # upload file to database
    # toDatabase.setFile('upload.json')
    # toDatabase.uploadFile()

    # if log in
    user = 92262870
    toDatabase = uploadToDB()
    keyCredential = encryptDecrypt()
    if toDatabase.checkID(user):
        keyCredential.setKey(toDatabase.getKey(user))

    # download file from database
    toDatabase.downloadFile(user)

    # TODO: check if the data in local is the same as the data in database

    # decrypt file using key
    keyCredential.decryptFile("data.json")

