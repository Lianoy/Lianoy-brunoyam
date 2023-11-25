import asyncio

async def test():
    i = 0
    while True:
        print(i)
        i += 1
        await asyncio.sleep(1)

async def sec ():
    count = 0
    while True:
        if count % 3 == 0:
            print ("Прошло три секунды")
        count += 1
        await asyncio.sleep(1)

async def thr ():
    count = 0
    while True:
        if count % 5 == 0:
            print ("Прошло пять секунд")
        count += 1
        await asyncio.sleep(1)

async def main():
    task = [asyncio.create_task(test()),asyncio.create_task(sec()),asyncio.create_task(thr())]
    await asyncio.gather(*task)

asyncio.run(main())

