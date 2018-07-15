from collections import namedtuple

Result = namedtuple('Result', ['count', 'average'])


def average():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield
        if term is None:
            break
        total += term
        count += 1
        average = total / count
    # Before python3.3 return course error if generator return result.
    return Result(count, average)


if __name__ == '__main__':
    coro_avg = average()
    next(coro_avg)
    coro_avg.send(10)
    coro_avg.send(30)
    coro_avg.send(6.5)
    coro_avg.send(None)  # 发送None会终止循环，导致协程结束抛出StopIteration异常，value中保存返回值
# StopIteration: Result(count=3, average=15.5)
