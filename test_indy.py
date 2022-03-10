import asyncio
from functools import reduce
import json
import random
import string
import time
from enum import Enum
from indy import wallet, error
from ctypes import cdll
import platform

EXTENSION = {"darwin": ".dylib", "linux": ".so", "win32": ".dll", 'windows': '.dll'}

KEY_LENGTH = 32

class KeyDerivationMethod(Enum):

    argon = "ARGON2I_MOD"
    raw = "RAW"


async def create():
    key = ''.join(
        random.SystemRandom().choice(
            string.ascii_letters + string.digits
        ) for _ in range(KEY_LENGTH)
    )
    config = {
        "id": key,
        "key_derivation_method": KeyDerivationMethod.argon.value,
        "storage_type": "postgres_storage",
        "storage_config": {"url":"db:5432"}
    }
    credentials = {
        "key": key,
        "storage_credentials": {
            "account": "postgres",
            "password": "development",
            "admin_account": "postgres",
            "admin_password": "development"
        }
    }
    try:
        create_time = time.time()
        await wallet.create_wallet(
            config=json.dumps(config),
            credentials=json.dumps(credentials)
        )
        create_time = time.time() - create_time
        open_time = time.time()
        handle = await wallet.open_wallet(
            config=json.dumps(config), credentials=json.dumps(credentials)
        )
        open_time = time.time() - open_time
        return create_time, open_time
    except error.IndyError as err:
        print(err.message)
        raise


def file_ext():
  your_platform = platform.system().lower()
  return EXTENSION[your_platform] if (your_platform in EXTENSION) else '.so'


async def load_postgres():
  print("Initializing postgres wallet")
  stg_lib = cdll.LoadLibrary("libindystrgpostgres" + file_ext())
  result = stg_lib.postgresstorage_init()

async def main():
    await load_postgres()

    begin = time.time()

    times = []
    for _ in range(100):
        res = await create()
        times.append(res)


    end = time.time()
    print("Total:",end-begin)
    print("Average create:", reduce(lambda acc, val: acc + val[0], times, 0) / len(times))
    print("Average open:", reduce(lambda acc, val: acc + val[1], times, 0) / len(times))
    print("Average create + open:", reduce(lambda acc, val: acc + val[0] + val[1], times, 0) / len(times))



if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
