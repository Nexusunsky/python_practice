import time
from atexit import register
from random import randrange
from threading import Thread, Lock, BoundedSemaphore

lock = Lock()
MAX = 5
candytray = BoundedSemaphore(MAX)


def refill():
    lock.acquire()
    print('Refilling candy...')
    try:
        candytray.release()
    except ValueError:
        print('full,skipping')
    else:
        print('OK')
    lock.release()


def buy():
    lock.acquire()
    print('Buying candy...')
    if candytray.acquire(False):
        print('OK')
    else:
        print('empty,skipping')
    lock.release()


def producer(loops):
    for i in range(loops):
        refill()
        time.sleep(randrange(3))


def consumer(loops):
    for i in range(loops):
        buy()
        time.sleep(randrange(3))


def main():
    print('starting at:', time.ctime())
    nloops = randrange(2, 6)
    print('THE CANDY MACHINE ( full with %d bars)' % MAX)
    Thread(target=consumer, args=(nloops,)).start()
    Thread(target=producer, args=(nloops,)).start()


@register
def _at_exit():
    print('all DONE at:', time.ctime())


if __name__ == '__main__':
    main()
