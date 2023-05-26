import environs
from tortoise import Tortoise, run_async

env = environs.Env()
env.read_env(".env")


async def init():
    await Tortoise.init(
        db_url=str(env("DATABASE_URL")),
        modules={'models': ['database.database_table']}
    )

    await Tortoise.generate_schemas()

run_async(init())


