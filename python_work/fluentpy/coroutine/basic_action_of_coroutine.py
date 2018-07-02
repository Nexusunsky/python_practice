import inspect


def simple_coroutines():
    print(' -> Coroutines started')
    x = yield  # yield None
    print(' -> Coroutines received:', x)


def sample_16_1():
    my_coro = simple_coroutines()
    print(my_coro)
    print(next(my_coro))  # 等价<==>  my_coro.send(None) 预激（prime）
    my_coro.send(42)


def simple_coro2(a):
    print(' -> Started: a = ', a)
    b = yield a
    print(' -> Received: b =', b)
    c = yield a + b
    print(' -> Received: c =', c)


def sample_16_2():
    my_coro2 = simple_coro2(14)
    print(inspect.getgeneratorstate(my_coro2))
    next(my_coro2)
    print(inspect.getgeneratorstate(my_coro2))
    my_coro2.send(28)
    my_coro2.send(99)
    print(inspect.getgeneratorstate(my_coro2))


if __name__ == '__main__':
    sample_16_1()
    sample_16_2()
