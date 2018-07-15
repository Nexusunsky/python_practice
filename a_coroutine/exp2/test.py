from a_coroutine.exp2.sched import sleep, switch, run


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
    await switch()
    print("C2: c")
    await sleep(1)
    print("C2: Stop")


if __name__ == '__main__':
    run([coro1(), coro2()])
