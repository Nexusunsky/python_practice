from functools import wraps


# Method decorator
def use_logging(func):
    def wrapper():
        print("%s is running" % func.__name__)
        return func()

    return wrapper


def use_logging_with_para(func):
    def wrapper(name):
        print("%s is running" % func.__name__)
        return func(name)

    return wrapper


def use_logging_with_args(func):
    def wrapper(*args, **kwargs):
        print("%s is running" % func.__name__)
        return func(*args, **kwargs)

    return wrapper


def foo():
    print('I am foo')


# @ Syntactic sugar
@use_logging
def foo1():
    print('I am foo1')


@use_logging_with_para
def foo2(name):
    print('I am a %(e)s' % {'e': name})


@use_logging_with_args
def foo3(name, age=None, height=None):
    print('I am a %(e)s and %(age)d year\'s old , %(height)f m' % {'e': name, 'age': age, 'height': height})


# control method's level
def intercept_logging(level):
    def intercept(func):  # intercept start
        def wrapper(*args, **kwargs):  # wrapper start
            if level == "Warn":
                print("WARN: It \'s a warn message.")
            if level == "Info":
                print("INFO: It \'s a info message.")
            return func(*args, **kwargs)  # wrapper end

        return wrapper  # intercept end

    return intercept


@intercept_logging("Warn")
def foo_warn(name, age=None, height=None):
    print('I am a %(e)s and %(age)d year\'s old , %(height)f m' % {'e': name, 'age': age, 'height': height})


@intercept_logging("Info")
def foo_info(name, age=None, height=None):
    print('I am a %(e)s and %(age)d year\'s old , %(height)f m' % {'e': name, 'age': age, 'height': height})


# functools.warps
def logged(func):
    @wraps(func)  # Keep src method func info in decorator
    def with_logging(*args, **kwargs):
        print(func.__name__)
        print(func.__doc__)
        return func(*args, **kwargs)

    return with_logging


@intercept_logging("Info")
@logged
def f(x):
    """dose some math """
    result = x + x * x
    print("Result is %d" % result)
    return result


if __name__ == '__main__':
    foo = use_logging(foo)
    foo()
    foo1()
    foo2("Ne")
    foo3("Ne", 12, 1.75)
    foo_warn("Ne", 12, 1.75)
    foo_info("Ne", 12, 1.75)
    f(12)
