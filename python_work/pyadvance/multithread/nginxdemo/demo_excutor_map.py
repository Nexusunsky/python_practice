# Executor.map()
from concurrent import futures
from time import strftime, sleep


def display(*args):
    print(strftime('[%H:%M:%S]'), end=' ')
    print(*args)


def loiter(n):
    display('{}loiter({}): sleeping for {}s...'.format('\t' * n, n, n))
    sleep(n)
    display('{}loiter({}): done.'.format('\t' * n, n))
    return n * 10


def main():
    display('Script starting,')

    executor = futures.ThreadPoolExecutor(max_workers=3)
    result = executor.map(loiter, range(5))
    display('results:', result)

    display('Waiting for individual results:')
    for i, result in enumerate(result):
        display('result {}: {}'.format(i, result))


if __name__ == '__main__':
    main()
