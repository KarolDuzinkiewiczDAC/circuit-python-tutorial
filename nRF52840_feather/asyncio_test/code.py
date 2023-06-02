import asyncio


class TotalPrintCount:
    # simple object shared by many coroutines
    def __init__(self) -> None:
        self.value = 0


# definition of async coroutine
async def print_message(id, interval, count, total_print_count):
    for _ in range(count):
        total_print_count.value += 1
        print(f'ID: {id}, total print count: {total_print_count.value}')
        # wait for a little bit to allow the scheduler execute another task
        await asyncio.sleep(interval)


async def main():
    # create an object shared between 2 tasks
    total_print_count = TotalPrintCount()

    # create 2 async tasks (wrapping async coroutines)
    # NOTE: It is now the responsibility of the scheduler to start both tasks.
    print_task_1 = asyncio.create_task(print_message(1, 0.25, 10, total_print_count))
    print_task_2 = asyncio.create_task(print_message(2, 0.5, 10, total_print_count))
    # wait for all the listed tasks to finish
    await asyncio.gather(print_task_1, print_task_2)
    print("done")

asyncio.run(main())
