import inspect


def attr_from_locals(locals_dict):
    self = locals_dict.pop('self')
    args = inspect.getargspec(self.__init__.__func__).args[1:]
    for k in args:
        setattr(self, k, locals_dict[k])
    keywords = inspect.getargspec(self.__init__.__func__).keywords
    if keywords:
        keywords_dict = locals_dict[keywords]
        for k in keywords_dict:
            setattr(self, k, keywords_dict[k])


class Foo(object):
    def __init__(self, name, **kwargv):
        attr_from_locals(locals())


if __name__ == '__main__':
    f = Foo('bar', color='yellow', num=1)
    print(f.__dict__)
