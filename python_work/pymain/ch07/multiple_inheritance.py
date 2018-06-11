# Multiple inheritance
class Calculator(object):
    def calculate(self, expression):
        self.value = eval(expression)


class Talker(object):
    def talk(self):
        print('Hi, my value is ', self.value)


# Attention : if multi class implements the same super method,


# we should be careful about the order of the super class,
# cause the class before will override the after class on the same method
class TalkingCalculator(Calculator, Talker):
    pass


if __name__ == '__main__':
    tc = TalkingCalculator()
    tc.calculate('1+2+3')
    tc.talk()

    print(hasattr(tc, 'talk'))
    print(hasattr(tc, 'fnord'))

    print(callable(getattr(tc, 'talk', None)))
    print(callable(getattr(tc, 'fnord', None)))


