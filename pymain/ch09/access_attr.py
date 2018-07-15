# 可以拦截对对象属性的所有访问企图，其用途之一是在旧式类中实现特性(在旧式类中，函数property的行为可能不符合预期)。
# 要在属性被访问时执行一段代码，必须使用一些魔法方法。下面的四个魔法方法提供了你需要的所有功能(在旧式类中，只需使用后面三个)。
# __getattribute__(self, name):在属性被访问时自动调用(只适用于新式类)。
# __getattr__(self, name):在属性被访问而对象没有这样的属性时自动调用。
# __setattr__(self, name, value):试图给属性赋值时自动调用。
# __delattr__(self, name):试图删除属性时自动调用。

# 相比函数property，这些魔法方法使用起来要棘手些(从某种程度上说，效率也更低)，
# 但它们很有用，因为你可在这些方法中编写处理多个特性的代码。
# 然而，在可能的情况下，还是使用函数property吧。

# 前面说过，编写方法__setattr__时需要避开无限循环陷阱，编写__getattribute__时亦如此。
# 由于它拦截对所有属性的访问(在新式类中)，因此将拦截对__dict__的访问!
# 在__getattribute__中访问当前实例的属性时，唯一安全的方式是使用超类的方法__getattribute__(使用super)。


# A key difference between __getattr__ and __getattribute__

# is that __getattr__ is only invoked if the attribute wasn't found the usual ways.
# It's good for implementing a fallback for missing attributes, and is probably the one of two you want.

# __getattribute__ is invoked before looking at the actual attributes on the object,
# and so can be tricky to implement correctly. You can end up in infinite recursions very easily.


class Rectangle(object):
    def __init__(self):
        self.width = 0
        self.height = 0

    def __setattr__(self, key, value):
        print('set_attr', key, value)
        if key == 'size':
            self.width, self.height = value
        else:
            self.__dict__[key] = value

    def __getattr__(self, key):
        print('get_attr', key)
        if key == 'size':
            return self.width, self.height
        else:
            raise AttributeError()

    def __getattribute__(self, item):
        print('__getattribute__')
        super().__getattribute__(item)


if __name__ == '__main__':
    r = Rectangle()
    r.width = 10
    r.height = 5
    print(r.size)  # 非自有属性会执行__getattr__
    print(r.width)  # 自有属性不会执行__getattr__
