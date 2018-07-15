# Executor.map()
# map 函数返回结果的顺序与调用开始的顺序一致
# 为了实现 不管提交的顺序，只要有结果就获取，可以使用Executor.submit和 future.as_completed函数结合使用
from concurrent import futures
from time import strftime, sleep


def display(*args):
    print(strftime('[%H:%M:%S]'), end=' ')
    print(*args)


def loiter(n):
    display('{}loiter({}): sleeping for {}s...'.format('\t' * n, n, n))
    sleep(n)  # 耗时操作
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
