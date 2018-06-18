def yield_test(n):
    for i in range(n):
        yield call(i)
        print("i=", i)
    print("do something.")
    print("end.")


def call(i):
    return i * 2


def g():
    print('1')
    x = yield 'hello'
    print('2', 'x=', x)
    y = 5 + (yield x)
    print('3', 'y=', y)


if __name__ == '__main__':
    f = g()
    f.send(None)
    f.send(5)
    f.send(2)
    # for i in yield_test(5):
    #     print(i, ",")
