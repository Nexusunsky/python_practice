from functools import wraps
from inspect import getgeneratorstate


def coroutine(func):
    @wraps(func)
    def primer(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen

    return primer


@coroutine
def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total / count


def sample_16_4():
    coro_avg = averager()
    print(next(coro_avg))
    print(coro_avg.send(10))
    print(coro_avg.send(30))
    print(coro_avg.send(5))


def sample_16_5():
    coro_avg = averager()
    print(getgeneratorstate(coro_avg))
    print(coro_avg.send(10))
    print(coro_avg.send(30))
    print(coro_avg.send(5))


if __name__ == '__main__':
    sample_16_4()
    sample_16_5()
