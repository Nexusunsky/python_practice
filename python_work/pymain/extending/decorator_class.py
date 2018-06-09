# Decorator class


class Foo(object):
    def __init__(self, func):
        self._func = func

    def __call__(self):
        print('class decorator running')
        self._func()
        print('class decorator ending')


@Foo
def bar():
    print('bar')


if __name__ == '__main__':
    bar()
    f(2)
