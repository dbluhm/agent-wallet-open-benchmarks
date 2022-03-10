import asyncio
from functools import reduce
import random
import string
import time
from enum import Enum
from typing import Callable
from aries_askar import Store
from aries_askar.bindings import generate_raw_key
from os import getenv

EXTENSION = {"darwin": ".dylib", "linux": ".so", "win32": ".dll", 'windows': '.dll'}

REPO_URI = getenv("REPO_URI", "postgres://postgres:development@db:5432/")
KEY_LENGTH = 32

class KeyDerivationMethod(Enum):

    argon = "kdf:argon2i:mod"
    raw = "RAW"


def random_str(length: int) -> str:
    return ''.join(
        random.SystemRandom().choice(
            string.ascii_letters + string.digits
        ) for _ in range(length)
    )


async def create(name: str, key: str, method: KeyDerivationMethod):
    try:
        create_time = time.time()
        store = await Store.provision(f"{REPO_URI}{name}", method.value, key)
        create_time = time.time() - create_time
        await store.close()
    except Exception as err:
        print(err)
        raise
    return create_time


async def create_raw(name: str):
    return await create(f"raw{name}", generate_raw_key(), KeyDerivationMethod.raw)


async def create_argon(name: str):
    return await create(f"argon{name}", random_str(32), KeyDerivationMethod.argon)


async def time_creation(header: str, create_method: Callable, iterations: int):
    begin = time.time()

    times = []
    for i in range(iterations):
        res = await create_method(i)
        times.append(res)


    end = time.time()
    print(header)
    print("Total:",end-begin)
    print("Average:", reduce(lambda acc, val: acc + val, times, 0) / len(times))


async def main():
    await time_creation("Raw", create_raw, 10)
    await time_creation("Argon2i Mod", create_argon, 10)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
