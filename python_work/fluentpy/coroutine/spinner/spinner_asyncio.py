#!/usr/bin/env python3

# spinner_asyncio.py

# credits: Example by Luciano Ramalho inspired by
# Michele Simionato's multiprocessing example in the python-list:
# https://mail.python.org/pipermail/python-list/2009-February/538048.html

# BEGIN SPINNER_ASYNCIO
import asyncio
import itertools
import sys


# 使用线程进行并发编程时，需要程序员使用锁实现线程的同步，必须记住保留锁，去保护程序的重要部分，防止多步操作中的执行中断，防止数据处于无效。
# 协程默认会做好保护，防止中断，任意时刻都只有一个协程在运行，并且是主动让出控制权，便可以安全的控制中断.


@asyncio.coroutine  # <1>
def spin(msg):  # <2>
    write, flush = sys.stdout.write, sys.stdout.flush
    for char in itertools.cycle('|/-\\'):
        status = char + ' ' + msg
        write(status)
        flush()
        write('\x08' * len(status))
        try:
            yield from asyncio.sleep(.1)  # <3>
        except asyncio.CancelledError as error:  # <4>
            print('CancelledError : %s' % error)
            break
    write(' ' * len(status) + '\x08' * len(status))


@asyncio.coroutine
def slow_function():  # <5>
    # pretend waiting a long time for I/O
    yield from asyncio.sleep(3)  # <6> 把控制权交还给主循环，休眠结束后恢复这个协程
    return 42


@asyncio.coroutine
def supervisor():  # <7>
    spinner = asyncio.async(spin('thinking!'))  # <8> 排定spin协程的运行时间，使用Task对象包装spin协程，并立即返回。

    print('spinner object:', spinner)  # <9>  spinner object:
    # <Task pending coro=<spin() running at ~/fluentpy/coroutine/spinner/spinner_asyncio.py:15>>

    result = yield from slow_function()  # <10> 驱动slow_function函数，结束后，获取返回值。
    # 同时，事件循环继续，等待 交换控制权给主循环之后的返回

    spinner.cancel()  # <11> Task对象可以取消，取消后，会在协程当前暂停的yield处抛出asyncio.CancelledError
    return result


def main():
    loop = asyncio.get_event_loop()  # <12> 获取 事件循环
    result = loop.run_until_complete(supervisor())  # <13> 使用事件循环驱动协程的运行
    loop.close()
    print('Answer:', result)


if __name__ == '__main__':
    main()
# END SPINNER_ASYNCIO
