from inspect import getgeneratorstate

from fluentpy.coroutine.pratice_for_coroutine import averager


# 终止协程的一种方式，发生某个哨符值，让协程退出，内置的None和Ellipsis等常量经常用作哨符值

def sample_16_7():
    coro_avg = averager()
    coro_avg.send(40)
    coro_avg.send(50)
    coro_avg.send('spam')
    coro_avg.send(60)


class DemoException(Exception):
    pass


def demo_exc_handling():
    print(' -> coroutine started')
    while True:
        try:
            x = yield
        except DemoException:
            print('*** DemoException handled. Continuing...')
        else:
            print(' -> coroutine received: {!r}'.format(x))
    return RuntimeError('This line should never run')


def demo_exc_handling_finally():
    print(' -> coroutine started')
    try:
        while True:
            try:
                x = yield
            except DemoException:
                print('*** DemoException handled. Continuing...')
            else:
                print(' -> coroutine received: {!r}'.format(x))
    finally:
        print('-> coroutine ending')


def sample_16_10():
    exc_coro = demo_exc_handling()
    next(exc_coro)
    exc_coro.send(11)
    exc_coro.throw(DemoException)
    print(getgeneratorstate(exc_coro))


def sample_16_11():
    exc_coro = demo_exc_handling()
    next(exc_coro)
    exc_coro.send(11)
    exc_coro.throw(ZeroDivisionError)
    print(getgeneratorstate(exc_coro))


def sample_16_12():
    exc_coro = demo_exc_handling_finally()
    next(exc_coro)
    exc_coro.send(11)
    exc_coro.throw(ZeroDivisionError)
    print(getgeneratorstate(exc_coro))


if __name__ == '__main__':
    sample_16_12()
