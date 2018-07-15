import time
from time import sleep

from pyadvance.multithread.threading_demo3 import MyThread


def fib(x):
    sleep(0.005)
    if x < 2:
        return 1
    return fib(x - 2) + fib(x - 1)


def fac(x):
    sleep(0.1)
    if x < 2:
        return 1
    return x * fac(x - 1)


def sum(x):
    sleep(0.1)
    if x < 2:
        return 1
    return x + sum(x - 1)


funcs = [fib, fac, sum]
n = 12

if __name__ == '__main__':
    fun_times = range(len(funcs))

    print('###### Single Thread #######')
    for i in fun_times:
        print(' starting ', funcs[i].__name__, ' at: ', time.ctime())
        print(funcs[i](n))
        print(' finishing ', funcs[i].__name__, ' at: ', time.ctime())

    print('###### Multi Thread #######')
    threads = []
    for i in fun_times:
        t = MyThread(func=funcs[i], name=str(funcs[i].__name__ + 'Thread'), args=(n,))
        threads.append(t)

    for i in fun_times:
        threads[i].start()

    for i in fun_times:
        threads[i].join()
        print(threads[i].getResult())

    print('all DONE')
