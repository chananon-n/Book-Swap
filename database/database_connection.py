import environs
from tortoise import Tortoise

env = environs.Env()
env.read_env(".env")


async def init():
    await Tortoise.init(
        db_url=str(env("DATABASE_URL")),
        modules={'models': ['database.database_table']}
    )

    await Tortoise.generate_schemas()


