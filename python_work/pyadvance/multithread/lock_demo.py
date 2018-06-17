import time
from atexit import register
from random import randrange
from threading import currentThread, Thread, Lock


class CleanOutputSet(set):
    def __str__(self):
        return ', '.join(x for x in self)


lock = Lock()
# figure out Generator
loops = (randrange(2, 5) for x in range(randrange(3, 7)))
remaining = CleanOutputSet()


# context manager for simplify lock code
def loop_with(n_sec):
    myname = currentThread().name
    with lock:
        remaining.add(myname)
        print('[%s] started %s' % (time.ctime(), myname))

    time.sleep(n_sec)

    with lock:
        remaining.remove(myname)
        print('[%s] completed %s (%d secs)' % (time.ctime(), myname, n_sec))
        print(' #### (remaining: %s) #### ' % (remaining or 'NONE'))


def loop(n_sec):
    myname = currentThread().name

    lock.acquire()
    remaining.add(myname)
    print('[%s] started %s' % (time.ctime(), myname))
    lock.release()

    time.sleep(n_sec)

    lock.acquire()
    remaining.remove(myname)
    print('[%s] completed %s (%d secs)' % (time.ctime(), myname, n_sec))
    print(' #### (remaining: %s) #### ' % (remaining or 'NONE'))
    lock.release()


def main():
    print(loops)
    for pause in loops:
        Thread(target=loop_with, args=(pause,)).start()


@register
def __at_exit():
    print('All DONE at:', time.ctime())


if __name__ == '__main__':
    main()
