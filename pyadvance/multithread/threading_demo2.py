# newInstance of a thread , then transfer it a callable instance.
import threading
import time

loops = [4, 2]


class ThreadFunc(object):

    def __init__(self, func, args, name=''):
        self.name = name
        self.func = func
        self.args = args

    def __call__(self):
        self.func(*self.args)


def loop(n_loops, n_sec):
    print('start loop', n_loops, 'at:', time.ctime())
    time.sleep(n_sec)
    print('loop', n_loops, 'done at', time.ctime())


def main():
    print('starting at:', time.ctime())
    threads = []
    n_loops = range(len(loops))

    for i in n_loops:
        thread = threading.Thread(
            target=ThreadFunc(name=str(i), func=loop, args=(i, loops[i]))
        )
        threads.append(thread)

    for i in n_loops:
        threads[i].start()

    for i in n_loops:
        threads[i].join()

    print('add DONE at:', time.ctime())


if __name__ == '__main__':
    main()
