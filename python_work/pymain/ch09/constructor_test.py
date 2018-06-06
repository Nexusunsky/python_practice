class Bird:
    def __init__(self):
        self.hungry = True

    def eat(self):
        if self.hungry:
            print('I am hungry!')
        else:
            print('No I am Ok.')


class SongBird(Bird):
    """解决历史遗留问题。在较新的Python版本中，显然应使用函数 super"""

    def __init__(self):
        Bird.__init__(self)  # 指明使用超类的构造函数来，初始化 并传入的是当前对象的实例
        self.isSong = True

    def song(self):
        if self.isSong:
            print('I can song.')


# 使用函数super比调用超类的未关联构造函 数(或其他方法)要好得多。
# 函数super返回的到底是什么呢?通常，你无需关心这个问题，只管假定它返回你所需的 超类即可。
# 实际上，它返回的是一个super对象，这个对象将负责为你执行方法解析。
# 当你访问它的属性时，它将在所有的超类(以及超类的超类，等等)中查找，直到找到指定的属性或 引发AttributeError异常。

class IdiotBird(Bird):
    """ 调用这个函数时，将当前类和当前实例作为参数。对其返回的对象调用方 法时，调用的将是超类(而不是当前类)的方法。 """

    def __init__(self):
        super().__init__()
        self.hungry = False

    def idiot(self):
        if self.hungry:
            print('I am a Idiot.')


if __name__ == '__main__':
    SongBird().song()
    IdiotBird().eat()
