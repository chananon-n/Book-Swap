import os
import json

from library.Book import Book
from library.eBook import eBook


# convert abstractBook to json and save it to BookSwap resource
def save_book_to_resource(book):
    # check if BookSwap resource directory exist
    if not os.path.exists('BookSwap resources'):
        # create BookSwap resource directory
        os.mkdir('BookSwap resources')
    # check if book or ebook
    if isinstance(book, Book):
        # if book, create json file with bookID
        json_file = open('BookSwap resources/' + "Book" + str(book.getBookID()) + '.json', 'w')
    elif isinstance(book, eBook):
        # if ebook, create json file with ebookID
        json_file = open('BookSwap resources/' + "eBook" + str(book.getBookID()) + '.json', 'w')
    # convert book to json
    json_book = book.to_json()
    # create json file with
    json.dump(json_book, json_file, indent=4)




def load_book_from_resource():
    # get all file .json in BookSwap resources
    json_files = [pos_json for pos_json in os.listdir('BookSwap resources') if pos_json.endswith('.json')]
    # create book list
    book_list = []
    #clear book list
    book_list.clear()
    # loop once for each json file
    for json_file in json_files:
        # if book start with Book
        if json_file.startswith('Book'):
            # get bookID
            bookID = json_file[4:-5]
            # open json file
            json_file = open('BookSwap resources/' + json_file, 'r')
            # convert json to book
            book = Book.from_json(json.load(json_file))
            # set bookID
            book.setBookID(bookID)
            # add book to book list
            book_list.append(book)
        # if book start with eBook
        elif json_file.startswith('eBook'):
            # get ebookID
            ebookID = json_file[5:-5]
            # open json file
            json_file = open('BookSwap resources/' + json_file, 'r')
            # convert json to ebook
            ebook = eBook.from_json(json.load(json_file))
            # set ebookID
            ebook.setBookID(ebookID)
            # add ebook to book list
            book_list.append(ebook)
    return book_list


def json_to_book(json_file):
    # if json name start with Book
    if json_file.startswith('Book'):
        # get bookID
        bookID = json_file[4:-5]
        # open json file
        json_file = open('BookSwap resources/' + json_file, 'r')
        # convert json to book
        book = Book.from_json(json.load(json_file))
        # set bookID
        book.setBookID(bookID)
        return book
    # if json name start with eBook
    elif json_file.startswith('eBook'):
        # get ebookID
        ebookID = json_file[5:-5]
        # open json file
        json_file = open('BookSwap resources/' + json_file, 'r')
        # convert json to ebook
        ebook = eBook.from_json(json.load(json_file))
        # set ebookID
        ebook.setBookID(ebookID)
        return ebook


# create BookSwap resource directory
def create_resource_directory():
    if not os.path.exists('BookSwap resources'):
        os.makedirs('BookSwap resources')
        return True
    return False
