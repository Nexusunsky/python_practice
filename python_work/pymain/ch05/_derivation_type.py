from math import sqrt

# 列表推导是一种从其他列表创建列表的方式，类似于数学中的集合推导。
# 列表推导的工作原理非常简单，有点类似于for循环。

print([x * x for x in range(10)])
print([x * x for x in range(10) if x % 3 == 0])

girls = ['alice', 'bernice', 'clarice']
boys = ['chris', 'arnold', 'bob']
print([b + '+' + g for b in boys for g in girls if b[0] == g[0]])

# 前述男孩/女孩配对示例的效率不太高，因为它要检查每种可能的配对
# 创建这个字典后，列表推导遍历所有的男孩，并查找名字首字母与当前男孩相同的所有女孩。
# 这样，这个列表推导就无需尝试所有的男孩和女孩组合并检查他们的名字首字母是否相同了
girls = ['alice', 'bernice', 'clarice']
boys = ['chris', 'arnold', 'bob']
letterGirls = {}
for girl in girls:
    letterGirls.setdefault(girl[0], []).append(girl)
print([b + '+' + g for b in boys for g in letterGirls[b[0]]])  # 使用dict的方式直接从字典里面区相应的key-value，减少反复比较判断

# 使用圆括号代替方括号并不能实现元组推导，而是将创建生成器，详细信息请参阅第9章的 旁注“简单生成器”。
# 然而，可使用花括号来执行字典推导。
squares = {i: "{} squared is {}".format(i, i ** 2) for i in range(10)}
print(squares[8])

# 使用exec和eval执行字符串及计算其结果
# 动态地编写Python代码，并将其作为语句进行执行或作为表达式进行计算。
# 命名空间——用于放置变量的地方;否则代码将污染你的命名空间，即修改你的变量。
# 函数exec主要用于动态地创建代码字符串。
# 命名空间视为放置变量的地方，类似于一个看不见的字典。
# 因此，当你执行赋值语句x = 1 时，将在当前命名空间存储键x和值1。
# 当前命名空间通常是全局命名空间(到目前为止，我们使用的大都是全局命名空间)，但并非必然如此。
scope = {}
exec('sqrt = 1', scope)
print(sqrt(4))
print(scope['sqrt'])
print(len(scope))
print(scope.keys())  # 自动在其中添加 了包含所有内置函数和值的字典__builtins__。

# exec执行一系列Python语句，而eval计算用字符串表示的Python表达式的值，
# 并返回结果(exec什么都不返回，因为它本身是条语句)。
# 向exec或eval提供命名空间时，可在使用这个命名空间前在其中添加一些值。
scope = {'x': 2, 'y': 3}
print(eval('x * y', scope))
# 同样，同一个命名空间可用于多次调用exec或eval。
scope = {}
exec('x = 2', scope)
print(eval('x * x', scope))
