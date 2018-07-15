import time
import _thread

loops = [4, 2]


def loop(n_loops, n_sec, lock):
    print('start loop', n_loops, 'at:', time.ctime())
    time.sleep(n_sec)
    print('loop', n_loops, 'done at', time.ctime())
    lock.release()


def main():
    print('starting at:', time.ctime())

    locks = []
    n_loops = range(len(loops))
    for i in n_loops:
        lock = _thread.allocate_lock()
        lock.acquire()
        locks.append(lock)
    for i in n_loops:
        _thread.start_new_thread(loop, (i, loops[i], locks[i]))
    for i in n_loops:
        while locks[i].locked():
            pass

    print('all Done at:', time.ctime())


if __name__ == '__main__':
    main()
