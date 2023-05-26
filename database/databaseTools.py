import random
from database.database_table import ID_NAME, BookID_BName, ID_BookID_Status


# create user id and name
async def create_id_name(name):
    # random id from 10000000 to 99999999
    rand_id = random.randint(1000000, 99999999)
    # loop until id is not in database
    while await ID_NAME.exists(id=rand_id):
        rand_id = random.randint(10, 1000)
        # create id and name
    id_name = ID_NAME(id=rand_id, name=name)
    await id_name.save()
    return rand_id


# check id
async def check_id(input_id):
    # check if id is in database, return None if it is not
    return await ID_NAME.exists(id=input_id)


# get name by id
async def get_name(input_id):
    # check if id is in database, return None if it is not
    return await ID_NAME.exists(id=input_id)


# create book id and name
async def create_book_id_name(name):
    # random id from 10 to 1000
    rand_id = random.randint(10, 1000)
    # loop until id is not in database
    while await BookID_BName.exists(bookId=rand_id):
        rand_id = random.randint(10, 1000)

    book_id_name = BookID_BName(bookId=rand_id, bookName=name)
    await book_id_name.save()


# edit book name by id
async def edit_book_name(input_id, input_name):
    # check if id is in database, return None if it is not
    if await BookID_BName.exists(bookId=input_id):
        # return name
        book_id_name = await BookID_BName.get(bookId=input_id)
        book_id_name.bookName = input_name
        await book_id_name.save()
        return True
    return False


# get book name by id
async def get_book_name(input_id):
    # check if id is in database, return None if it is not
    if await BookID_BName.exists(bookId=input_id):
        # return name
        book_id_name = await BookID_BName.get(bookId=input_id)
        return book_id_name.bookName
    return False


# getbook id by name
async def get_book_id(input_name):
    # check if name is in database, return None if it is not
    if await BookID_BName.exists(bookName=input_name):
        # return id
        book_id_name = await BookID_BName.get(bookName=input_name)
        return book_id_name.bookId
    return False


# create book status
async def create_book_status(book_id, user_id, status):
    # check if book id and user id is in database, return None if it is not
    if await ID_BookID_Status.exists(bookId_id=book_id, userId_id=user_id):
        # return status
        book_status = await ID_BookID_Status.get(bookId_id=book_id, userId_id=user_id)
        return book_status.status
    # create book status
    book_status = ID_BookID_Status(bookId_id=book_id, userId_id=user_id, status=status)
    await book_status.save()


# get book status by book id and user id
async def get_book_status(book_id, user_id):
    # check if book id and user id is in database, return None if it is not
    if await ID_BookID_Status.exists(bookId_id=book_id, userId_id=user_id):
        # return status
        book_status = await ID_BookID_Status.get(bookId_id=book_id, userId_id=user_id)
        return book_status.status
    return False


# remove row from ID_BookID_Status
async def remove_book_status(book_id, user_id):
    # check if book id and user id is in database, return None if it is not
    if await ID_BookID_Status.exists(bookId_id=book_id, userId_id=user_id):
        # return status
        book_status = await ID_BookID_Status.get(bookId_id=book_id, userId_id=user_id)
        await book_status.delete()
        return True
    return False


async def get_all_book(command, user_id):
    # check if user id is in database, return None if it is not
    if await ID_NAME.exists(id=user_id):
        if command == "borrow":
            # return all book id and name that user borrowed
            book_status = await ID_BookID_Status.filter(userId_id=user_id, status=0)
            return book_status
        elif command == "available":
            # return all book id and name that user can borrow
            book_status = await ID_BookID_Status.filter(userId_id=user_id, status=1)
            return book_status
        elif command == "all":
            # return all book id and name
            book_status = await ID_BookID_Status.filter(userId_id=user_id)
            return book_status
    return False


# run_async(init())
# a = asyncio.run(check_id(659))
# print(a)
# run_async(create_id_name("test"))
# print(asyncio.run(get_name(659)))
# run_async(create_book_id_name("book1"))
# print(asyncio.run(get_book_id("book1")))
# print(asyncio.run(get_book_name(624)))
# run_async(create_book_status(624, 659, 0))
# print(asyncio.run(get_book_status(624, 659)))

# run_async(create_id_name("test2"))
# print(asyncio.run(get_name(654)))
# run_async(create_book_id_name("book2"))
# print(asyncio.run(get_book_id("book2")))
# print(asyncio.run(get_book_name(492)))
# run_async(create_book_status(492, 654, 1))
# print(asyncio.run(get_book_status(492, 654)))

# run_async(create_book_status(624, 654, 0))
# run_async(remove_book_status(492, 654))
