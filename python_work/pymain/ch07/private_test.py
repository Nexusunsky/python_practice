from pymain.ch07.test_py import CTest


class ObjectInstance(object):
    def _test_one(self):
        print("I am a method has one _")

    def __test_two(self):
        print("I am a method has two _")


if __name__ == '__main__':
    CTest().c_method()
