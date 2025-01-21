import asyncio


async def start_strongman(name, power):
    
    print(f'Силач {name} начал соревнования')
    for i in range(5):
        await asyncio.sleep(1 / power)
        print(f'Силач {name} поднял {i + 1} шар')
    print(f'Силач {name} закончил соревнования.')


async def start_tournament():
    h1 = asyncio.create_task(start_strongman('Pasha', 3))
    h2 = asyncio.create_task(start_strongman('Denis', 4))
    h3 = asyncio.create_task(start_strongman('Apollon', 5))
    await h1
    await h2
    await h3


if __name__ == '__main__':
    asyncio.run(start_tournament())