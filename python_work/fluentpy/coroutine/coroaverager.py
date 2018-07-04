from collections import namedtuple
from inspect import getgeneratorstate

Result = namedtuple('Result', ['count', 'average'])


# Conclude :
# 1,子生成器不终止，委派生成器会在yield from 表达式处永远暂停
# 2,委派生成器相当于管道，一个委派生成器yield from 调用另一个子生成器，以此类推，
# 最终，这个链条要以一个只使用yield表达式的简单生成器结束

# child Gen
def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield
        if term is None:
            break
        total += term
        count += 1
        average = total / count
    return Result(count, average)


# delegate Gen
def grouper(results, key):
    # grouper发送的每个值都会经由 yield from 处理，通过管道传给averager实例
    # grouper会在yield from表达式处暂停，等待 averager 实例处理客户端发来的值
    # averager实例运行完毕以后，返回值绑定到results[key]上
    # 每次循环创建一个新的averager()对象
    while True:
        results[key] = yield from averager()  # GET_YIELD_FROM_ITER


# Client
def main(data):
    results = {}
    for key, values in data.items():
        group = grouper(results=results, key=key)

        print(group)
        print(getgeneratorstate(group))

        next(group)  # prime

        print(getgeneratorstate(group))

        for value in values:
            group.send(value)

        group.send(None)
        print(getgeneratorstate(group))
        print('Get here.')

    print(results)
    report(results=results)


def report(results):
    for key, result in sorted(results.items()):
        group, unit = key.split(';')
        print('{:2} {:5} averaging {:.2f}{}'.format(
            result.count, group, result.average, unit)
        )


data = {
    'girls;kg':
        [40.9, 38.5, 44.3, 42.2, 45.2, 41.7, 44.5, 38.0, 40.6, 44.5],
    'girls;m':
        [1.6, 1.51, 1.4, 1.3, 1.41, 1.39, 1.33, 1.46, 1.45, 1.43],
    'boys;kg':
        [39.0, 40.8, 43.2, 40.8, 43.1, 38.6, 41.4, 40.6, 36.3],
    'boys;m':
        [1.38, 1.5, 1.32, 1.25, 1.37, 1.48, 1.25, 1.49, 1.46],
}

if __name__ == '__main__':
    main(data=data)
    # dis.dis(grouper)
    # dis.dis(averager)
