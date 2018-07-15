class Rectangle(object):
    def __init__(self):
        self.width = 0
        self.height = 0

    def set_size(self, size):
        self.width, self.height = size

    def get_size(self):
        return self.width, self.height


# 在组合已有属性成为一个新的属性
# 使用 函数Property实现：仅仅考虑size属性，而其相关系的width和height动态计算
# 使用新式类中保证property的正确性
# property其实并不是函数，而是一个类。它的实例包含一些魔法方法，而所有的魔法都 是由这些方法完成的。
# 这些魔法方法为__get__、__set__和__delete__，它们一道定义了所谓的描述符协议。
# 只要对象实现了这些方法中的任何一个，它就是一个描述符。描述符的独特之处在于其访问方式。
class PropRectangle(object):

    def __init__(self):
        self.width = 0
        self.height = 0

    def set_size(self, size):
        self.width, self.height = size

    def get_size(self):
        return self.width, self.height

    def del_size(self):
        del self.width, self.height

    size = property(fget=get_size, fset=set_size, fdel=del_size, doc='Test Property for size')


if __name__ == '__main__':
    r = Rectangle()
    r.width = 10
    r.height = 5
    print(r.get_size())
    r.set_size((150, 100))
    print(r.width)

    r2 = PropRectangle()
    r2.width = 100
    r2.height = 50
    print(r2.size)
    r2.size = 10, 5
    print(r2.width)
    del r2.size
    print(r2.width)
