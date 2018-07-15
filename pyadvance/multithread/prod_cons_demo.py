import random
import time
from atexit import register
from queue import Queue

from pyadvance.multithread.threading_demo3 import MyThread


def writeQ(queue):
    print('producing Value xxx for Q...')
    queue.put('xxx', 1)
    print('size now', queue.qsize())


def readQ(queue):
    val = queue.get(1)
    print('consumed Value (%s) from Q ...' % val, queue.qsize())
    print('size now', queue.qsize())


def writer(queue, loops):
    for i in range(loops):
        writeQ(queue)
        time.sleep(random.randint(1, 3))


def reader(queue, loops):
    for i in range(loops):
        readQ(queue)
        time.sleep(random.randint(2, 5))


funcs = [writer, reader]
n_funcs = range(len(funcs))


def main():
    n_loops = random.randint(2, 5)
    q = Queue(32)
    print(' Loops for ' + str(n_loops))

    threads = []
    for i in n_funcs:
        t = MyThread(func=funcs[i], args=(q, n_loops), name=funcs[i].__name__)
        threads.append(t)

    for i in n_funcs:
        threads[i].start()

    for i in n_funcs:
        threads[i].join()


if __name__ == '__main__':
    main()


@register
def _at_exit():
    print('all DONE at:', time.ctime())
