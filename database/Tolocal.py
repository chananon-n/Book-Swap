import os
import json

from library import abstractBook


# convert abstractBook to json and save it to BookSwap resource
def save_book_to_resource(book: abstractBook):
    # convert book to json
    book_json = json.dumps(book.__dict__)

    # save json to file
    with open(f'BookSwap resource/{type(book)}{book.book_id}.json', 'w') as file:
        file.write(book_json)


def load_book_from_resource():
    # get all file that start with Book or eBook
    files = [file for file in os.listdir('BookSwap resource') if file.startswith('Book') or file.startswith('eBook')]
    # get all json file
    json_files = [file for file in files if file.endswith('.json')]
    # convert json to Book or eBook
    books = [json_to_book(json_file) for json_file in json_files]
    # remove None
    books = [book for book in books if book is not None]
    return books


def json_to_book(json_file):
    # if json name start with Book
    if json_file.startswith('Book'):
        # convert json to Book
        return abstractBook.Book(json_file)
    # if json name start with eBook
    elif json_file.startswith('eBook'):
        # convert json to eBook
        return abstractBook.eBook(json_file)
    return None


# create BookSwap resource directory
def create_resource_directory():
    if not os.path.exists('BookSwap resource'):
        os.makedirs('BookSwap resource')
        return True
    return False
