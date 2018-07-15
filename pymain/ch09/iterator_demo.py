# 实现了方法__iter__的对象是可迭代的，而实现了方法__next__的对象是迭代器。
class Fibs:
    def __init__(self):
        self.a = 0
        self.b = 1

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a

    def __iter__(self):
        return self


class TestIterator(object):
    value = 0

    def __next__(self):
        self.value += 1
        if self.value > 10:
            raise StopIteration
        return self.value

    def __iter__(self):
        return self


if __name__ == '__main__':
    ti = TestIterator()
    print(list(ti))

    it = iter([1, 2, 3])
    print(it)
    print(next(it))
