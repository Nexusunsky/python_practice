# 给切变赋值
name = list('Perl')
print(name)
name[2:] = list('ar')
print(name)

name[1:] = list('ython')
print(name)

numbers = [1, 5]
print(numbers[1:1])
numbers[1:1] = [2, 3, 4]
print(numbers)
numbers[1:4] = []
print(numbers)
