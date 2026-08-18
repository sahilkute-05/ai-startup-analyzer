import asyncio
import time


async def task_one():
    print("Task 1 started")

    await asyncio.sleep(3)

    print("Task 1 finished")


async def task_two():
    print("Task 2 started")

    await asyncio.sleep(3)

    print("Task 2 finished")


async def main():

    start_time = time.time()

    await asyncio.gather(
        task_one(),
        task_two()
    )

    end_time = time.time()

    print(f"\nTotal time: {end_time - start_time:.2f} seconds")


asyncio.run(main())