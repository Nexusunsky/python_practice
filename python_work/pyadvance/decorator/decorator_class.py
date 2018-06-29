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


class NullDecl(object):
    def __init__(self, func):
        self.func = func
        for name in set(dir(func)) - set(dir(self)):
            setattr(self, name, getattr(func, name))

    def __call__(self, *args):
        return self.func(*args)


@NullDecl
def my_func(x, y, z):
    return (x + y) / z


if __name__ == '__main__':
    bar()
    print(my_func(1, 2, 3))
