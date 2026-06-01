import asyncio
import time


async def task(name):
    await asyncio.sleep(0.5)
    return f"{name} 完成"


async def main():
    start = time.perf_counter()
    r1, r2, r3 = await asyncio.gather(
        task("A"),
        task("B"),
        task("C"),
    )
    cost = time.perf_counter() - start
    print(r1, r2, r3)
    print(f"用了 {cost:.2f} 秒")


asyncio.run(main())
