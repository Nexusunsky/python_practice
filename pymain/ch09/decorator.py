class MyClass(object):

    @staticmethod
    def sMethod():
        print('This is a static a method.')

    # sMethod = staticmethod(sMethod)

    @classmethod
    def cMethod(cls):
        print('This is a class method of ', cls)

    # cMethod = classmethod(cMethod)

    def iMethod(self):
        print('This is a instance:', self)


if __name__ == '__main__':
    MyClass.sMethod()
    MyClass.cMethod()  # same as MyClass.cMethod(MyClass)
    MyClass().iMethod()
