# yield from x ：中对x做的第一件事情是：iter(x) 从中获取迭代器
# Syntax for Delegating to a Subgenerator'：把职责委托给子生成器的句法

# yield from的 主要功能是打开双向通道，把最外层的调用发与最内层的子生成器连接起来，这样两者可以直接发送和产出值，还可以直接传入异常
# 而不用在中间位置添加大量处理异常的样板代码，有了这个结构，协程可以通过以前不可能的方式委托职责


def chain(*iterables):
    for it in iterables:
        yield from it


if __name__ == '__main__':
    s = 'ABC'
    t = tuple(range(3))
    print(list(chain(s, t)))
