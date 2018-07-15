class Vector2d(object):

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r},{!r})'.format(class_name, *self)


if __name__ == '__main__':
    v1 = Vector2d(3, 4)
    print(eval(repr(v1)))
