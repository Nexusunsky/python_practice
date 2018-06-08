# 如果你创建覆盖整个列表的切片，得到的将是列表的副本。
names = ['Mrs. Entity', 'Mrs. Thing']
n = names[:]
# 现在n和names包含两个相等但不同的列表。
print(n is names)
print(n == names)
