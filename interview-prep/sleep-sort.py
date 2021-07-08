from asyncio import run, sleep, wait
from sys import argv

async def f(n):
    await sleep(n)
    print(n)

run(wait(list(map(f, map(int, argv[1:])))))
