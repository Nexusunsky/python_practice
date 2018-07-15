# Fake code

# RESULT = yield from EXPR
import sys


def fake_code():
    EXPR = []
    _i = iter(EXPR)  # 可迭代对象
    try:
        _y = next(_i)  # prime 生成子生成器对象
    except StopIteration as _e:
        _r = _e.value  # StopIteration _e.value 为迭代结果
    else:
        while True:  # 运行 循环时 委派生成器会阻塞，只做为调用端和下级生成器的通道
            try:
                _s = yield _y  # 产出子生成器当前元素，等待调用方发送_s中保存的值
            except GeneratorExit as _e:
                try:
                    _m = _i.close  # 调用方.close时，关闭委派生成器和子生成器
                except AttributeError:
                    pass
                else:
                    _m()
                raise _e
            except BaseException as _e:  # 处理 调用方.throw(exc_info) 传入的异常
                _x = sys.exc_info()
                try:
                    _m = _i.throw
                except AttributeError:
                    raise _e
                else:  # 将调用方传入的异常传入子生成器
                    try:
                        _y = _m(*_x)
                    except StopIteration as _e:
                        _r = _e.value
                        break
            else:  # 产出值没有异常
                try:
                    if _s is None:  # 调用方发送的是None 则在子生成器上调用 next() 否则调用 send()
                        _y = next(_i)
                    else:
                        _y = _i.send(_s)
                except StopIteration as _e:
                    _r = _e.value
                    break
    RESULT = _r  # 返回的结果即 整个yield from 的值
