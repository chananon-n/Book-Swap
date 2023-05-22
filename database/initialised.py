import asyncio

from tortoise import run_async

from database.database_connection import init
from database.database_table import ID_NAME, BookID_BName, ID_BookID_Status


async def create_id_name():
    id_name = ID_NAME(id=2, name='john')
    await id_name.save()


# get name by id
async def get_name(id):
    id_name = await ID_NAME.get(id=id)
    return id_name.name


run_async(init())
run_async(create_id_name())
# print(asyncio.run(get_name(1)))

