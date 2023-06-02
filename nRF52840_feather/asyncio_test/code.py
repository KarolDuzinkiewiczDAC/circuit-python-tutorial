import asyncio

async def print_message(id, interval, count):
        for _ in range(count):
            print(f'ID: {id}')
        await asyncio.sleep(interval)


async def main():
    print_task_1 = asyncio.create_task(print_message(1, 0.25, 3))
    await asyncio.gather(print_task_1)
    print("done")

asyncio.run(main())
