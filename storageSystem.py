from tortoise import run_async
import CustomExeptionalHandler as CEH
import database


class storageSystem:
    def __init__(self):
        run_async(database.init())

    def createNewUser(self, name):
        try:
            run_async(database.databaseTools.create_id_name(name))
        except CEH.databaseException as e:
            return e.message + "Error in createNewUser"
        return True

    def getUserName(self, id):
        try:
            return run_async(database.databaseTools.get_name(id))
        except CEH.databaseException as e:
            return e.message + "Error in getUserName"


