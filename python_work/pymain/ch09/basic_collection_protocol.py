# 序列和映射基本上是元素(item)的集合，要实现它们的基本行为(协议)，不可变对象需 要实现2个方法，而可变对象需要实现4个。
#  __len__(self):这个方法应返回集合包含的项数，对序列来说为元素个数，对映射来说为键值对数。
# 如果__len__返回零(且没有实现覆盖这种行为的__nonzero__)，对象在布尔上下文中将被视为假(就像空的列表、元组、字符串和字典一样)。
#
# __getitem__(self, key):这个方法应返回与指定键相关联的值。对序列来说，键应该是 0~n-1的整数(也可以是负数，这将在后面说明)，其中n为序列的长度。
# 对映射来说，键可以是任何类型。
#
#  __setitem__(self, key, value):这个方法应以与键相关联的方式存储值，以便以后能够使用__getitem__来获取。
# 当然，仅当对象可变时才需要实现这个方法。
#
# __delitem__(self, key):这个方法在对对象的组成部分使用__del__语句时被调用，应 删除与key相关联的值。
# 同样，仅当对象可变(且允许其项被删除)时，才需要实现这个方法。
#
# 对于这些方法，还有一些额外的要求。
#  对于序列，如果键为负整数，应从末尾往前数。换而言之，x[-n]应与x[len(x)-n]等效。 如果键的类型不合适(如对序列使用字符串键)，可能引发TypeError异常。
#  对于序列，如果索引的类型是正确的，但不在允许的范围内，应引发IndexError异常。
# 要了解更复杂的接口和使用的抽象基类(Sequence)


def check_index(key):
    """
    指定的键是否是可接受的索引?
    键必须是非负整数，才是可接受的。如果不是整数， 将引发TypeError异常;如果是负数，将引发Index Error异常(因为这个序列的长度是无穷的)
    """
    if not isinstance(key, int): raise TypeError
    if key < 0: raise IndexError


class ArithmeticSequence:
    def __init__(self, start=0, step=1):
        """
        初始化这个算术序列
        start -序列中的第一个值
        step -两个相邻值的差
        changed -一个字典，包含用户修改后的值
    """
        self.start = start
        self.step = step
        # 存储起始值 # 存储步长值
        self.changed = {}

    def __getitem__(self, key):
        """
        从算术序列中获取一个元素
        """
        check_index(key)
        try:
            return self.changed[key]
        except KeyError:
            return self.start + key * self.step

    def __setitem__(self, key, value):
        """
        修改算术序列中的元素
        """
        check_index(key)
        self.changed[key] = value


# 没有任何元素被修改
# 修改过?
# 如果没有修改过， # 就计算元素的值
# 存储修改后的值

if __name__ == '__main__':
    s = ArithmeticSequence(1, 2)
    print(s[4])
    s[4] = 2
    print(s[4])
    print(s[5])
