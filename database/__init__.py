from database.database_connection import init
from database.databaseTools import *


# run the init function to create the database
async def main():
    await init()
