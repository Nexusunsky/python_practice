# 代码块是一组语句，可在满足条件时执行(if语句)，可执行多次(循环)，等等。代码块是 通过缩进代码(即在前面加空格)来创建的。
# 注意:也可使用制表符来缩进代码块。
# Python将制表符解释为移到下一个制表位(相邻制表位相距8个空格)，
# 但标准(也是更佳的)做法是只使用空格(而不使用制表符)来缩进， 且每级缩进4个空格。

# 总之，==用来检查两个对象是否相等，而is用来检查两个对象是否相同(是同一个对象)。

# while 循环
name = ''
while not name:
    name = input('Please enter your name: ')

print('Hello, {}!'.format(name))

# for 循环
for number in range(1, 101):
    print(number)
# 提示 只要能够使用for循环，就不要使用while循环。

# 注意 字典元素的排列顺序是不确定的。
# 换而言之，迭代字典的键或值时，一定会处理所有的 键或值，但不知道处理的顺序。
# 如果顺序很重要，可将键或值存储在一个列表中并对列 表排序，再进行迭代。
d = {'x': 1, 'y': 2, 'z': 3}
for key in d:
    print(key, 'corresponds to', d[key])

names = ['anne', 'beth', 'george', 'damon']
ages = [12, 45, 32, 102]
for i in range(len(names)):
    print(names[i], 'is', ages[i], 'years old')
print(list(zip(names, ages)))

strings = 'Reading The fucking source code.'
for string in strings:
    if 'T' in string:
        index = strings.index(string)  # 在字符串列表中查找字符串 strings[index] = '[censored]'
        print(strings[index])

index = 0
for string in strings:
    if 'c' in string:
        print(strings[index])
        # strings[index] = ']'
    index += 1

for index, string in enumerate(strings):
    if 'r' in string:
        print(strings[index])
        # strings[index] = 'e'

values = sorted('Hello, World!')
iterator = reversed(values)
print(list(iterator))
print(''.join(iterator))
print(values[3])
print(values[3:7:1])
print(values)
