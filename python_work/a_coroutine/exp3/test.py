from a_coroutine.exp3.sched import switch, scheduler, sleep


async def coro1():
    print("C1: Start")
    await sleep(1)
    print("C1: a")
    await switch()
    print("C1: b")
    await switch()
    print("C1: c")
    await switch()
    print("C1: Stop")


async def coro2():
    print("C2: Start")
    await switch()
    print("C2: a")
    await switch()
    print("C2: b")
    scheduler.add_coro(coro3())
    await switch()
    print("C2: c")
    await sleep(1)
    print("C2: Stop")


async def coro3():
    print("C3: Start")
    await sleep(1)
    print("C3: a")
    await switch()
    print("C3: b")
    await switch()
    print("C3: c")
    await sleep(1)
    print("C3: Stop")


if __name__ == '__main__':
    scheduler.add_coro(coro1())
    scheduler.add_coro(coro2())
    scheduler.run()
