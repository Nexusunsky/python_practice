# 序列解包(可迭代对象解包)
value = 1, 2, 3
print(value)
x, y, z = value
print(x, y, z)

# 从字典中获取元组迭代对象，然后解包
scoundrel = {'name': 'Robin', 'girlfriend': 'Marion'}
key, val = scoundrel.popitem()
print(key, val)

# 在解包时 使用 * 来 展开多余的元组
a, b, *rest = [1, 2, 3, 4]
print(rest)

name = "Albus Percival Wufric Brian Dumbledore"
first, *middle, last = name.split()
print(middle)
