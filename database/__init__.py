from tortoise import run_async

from database.database_connection import init
from database.databaseTools import *

run_async(init())
