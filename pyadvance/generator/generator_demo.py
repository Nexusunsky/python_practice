# Two simple generator functions
from collections import deque


class TaskScheduler(object):
    def __init__(self):
        self._task_queue = deque()

    def new_task(self, task):
        '''
        Admit a newly started task to the scheduler
        '''
        self._task_queue.append(task)

    def run(self):
        '''
        Run until there are no more tasks
        '''
        while self._task_queue:
            task = self._task_queue.popleft()
            try:
                # Run until the next yield statement
                next(task)
                self._task_queue.append(task)
            except StopIteration:
                # Generator is no longer executing
                pass


def count_down(n):
    while n > 0:
        print('T-minus', n)
        yield
        n -= 1
    print('Blastoff!')


def count_up(n):
    x = 0
    while x < n:
        print('Counting up', x)
        yield
        x += 1


if __name__ == '__main__':
    # Example use
    sched = TaskScheduler()
    sched.new_task(count_down(10))
    sched.new_task(count_down(5))
    sched.new_task(count_up(15))
    sched.run()
