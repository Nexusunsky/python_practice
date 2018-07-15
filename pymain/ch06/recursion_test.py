#  这样的递归函数通常包含下面两部分。
#  基线条件(针对最小的问题):满足这种条件时函数将直接返回一个值。
#  递归条件:包含一个或多个调用，这些调用旨在解决问题的一部分。
#  这里的关键是，通过将问题分解为较小的部分，可避免递归没完没了，因为问题终将被分解 成基线条件可以解决的最小问题。


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)
