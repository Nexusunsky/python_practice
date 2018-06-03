import string

seq = ['1', '2', '3', '4', '5']
sep = '+'
print(sep.join(seq))

dirs = '', 'usr', 'bin', 'env'
print('/'.join(dirs))

print('C:' + '\\'.join(dirs))

# 词首大写
print("that's all folks".title())
print(string.capwords("that's all, folks"))

# 方法strip将字符串开头和末尾的空白(但不包括中间的空白)删除，并返回删除后的结果
print('*** SPAM * for * everyone!!! ***'.strip(' *!'))

# 方法translate与replace一样替换字符串的特定部分，但不同的是它只能进行单字符替换。
# 这个方法的优势在于能够同时替换多个字符，因此效率比replace高。
# 使用translate前必须创建一个转换表。这个转换表指出了不同Unicode码点之间的转 换关系。
table = str.maketrans('cs', 'kz', ' ')  # 将字符c和s分别替换为k和z，空格替换为None
print(table)
print('this is an incredible test'.translate(table))
