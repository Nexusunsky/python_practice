from pymain.ch07 import private_test


class CTest(object):
    # print("Class C being defined.")
    def c_method(self):
        print("C name is c_method")


def foo(x): return x * x


#  make it lambda
foo_lambda = lambda x: x + x


def print_name_of_instance_class():
    print(type(ins1).__name__)


if __name__ == '__main__':
    ins1 = private_test.ObjectInstance()
    ins1._test_one()
    # ins1.__test_two()
    print(foo(3))
    print(foo_lambda(3))
    print_name_of_instance_class()
