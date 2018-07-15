from collections import namedtuple
from inspect import getgeneratorstate

Result = namedtuple('Result', ['count', 'average'])


# Conclude :
# 1,子生成器不终止，委派生成器会在yield from 表达式处永远暂停
# 2,委派生成器相当于管道，一个委派生成器yield from 调用另一个子生成器，以此类推，
# 最终，这个链条要以一个只使用yield表达式的简单生成器结束


# PEP 380 Proposal:
# 1, “子生成器产出的值都直接传给委派生成器的调用方（即客户端代码）。

# 2, 使用 send() 方法发给委派生成器的值都直接传给子生成器。
# 如果发送的值是 None，那么会调用子生成器的 __next__() 方法。
# 如果发送的值不是 None，那么会调用子生成器的 send() 方法。
# 如果调用的方法抛出 StopIteration 异常，那么委派生成器恢复运行。任何其他异常都会向上冒泡，传给委派生成器。

# 3, 生成器退出时，生成器（或子生成器）中的 return expr 表达式会触发 StopIteration(expr) 异常抛出。

# 4, yield from 表达式的值是子生成器终止时传给 StopIteration 异常的第一个参数。

# ***** yield from 结构的另外两个特性与异常和终止有关:
# 1, “传入委派生成器的异常，除了 GeneratorExit 之外都传给子生成器的 throw() 方法。
# 如果调用 throw() 方法时抛出 StopIteration 异常，委派生成器恢复运行。
# StopIteration 之外的异常会向上冒泡，传给委派生成器。”

# 2, “如果把 GeneratorExit 异常传入委派生成器，或者在委派生成器上调用 close() 方法，那么在子生成器上调用 close() 方法，如果它有的话。
# 如果调用 close() 方法导致异常抛出，那么异常会向上冒泡，传给委派生成器；否则，委派生成器抛出 GeneratorExit 异常。”


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
