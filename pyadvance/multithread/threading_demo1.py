# newInstance of thread , then transfer a func to it.
import threading
import time

loops = [4, 2]


def loop(n_loops, n_sec):
    print('start loop', n_loops, 'at:', time.ctime())
    time.sleep(n_sec)
    print('loop', n_loops, 'done at', time.ctime())


def main():
    print('starting at:', time.ctime())
    threads = []
    n_loops = range(len(loops))

    for i in n_loops:
        t = threading.Thread(target=loop, args=(i, loops[i]))
        threads.append(t)

    for i in n_loops:
        threads[i].start()

    for i in n_loops:
        threads[i].join()

    print('add DONE at:', time.ctime())


if __name__ == '__main__':
    main()
