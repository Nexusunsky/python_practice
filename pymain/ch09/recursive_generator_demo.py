# 不迭代类似于字符串的对象:
def flatten(nested):
    result = []
    try:
        try:
            nested + ''
        except TypeError:
            pass
        else:  # 未发生异常时 为排除对于str类型的数据进行递归
            raise TypeError
        for sublist in nested:
            for element in flatten(sublist):
                result.append(element)
    except TypeError:
        result.append(nested)
    return result


def repeater(value):
    while True:
        new = (yield value)
        if new is not None: value = new
