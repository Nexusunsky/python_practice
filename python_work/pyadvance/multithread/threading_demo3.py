# extends thread to a subThread , then newInstance of the subThread
import threading
import time

loops = [4, 2]


class MyThread(threading.Thread):
    def __init__(self, func, args, name):
        super().__init__()
        self.name = name
        self.func = func
        self.args = args

    def run(self):
        self.result = self.func(*self.args)

    def getResult(self):
        return self.result


def loop(n_loops, n_sec):
    print('start loop', n_loops, 'at:', time.ctime())
    time.sleep(n_sec)
    print('loop', n_loops, 'done at', time.ctime())


def main():
    print('starting at:', time.ctime())
    threads = []
    n_loops = range(len(loops))

    for i in n_loops:
        thread = MyThread(func=loop, args=(i, loops[i]), name=str(i))
        threads.append(thread)

    for i in n_loops:
        threads[i].start()

    for i in n_loops:
        threads[i].join()

    print('add DONE at:', time.ctime())


if __name__ == '__main__':
    main()
