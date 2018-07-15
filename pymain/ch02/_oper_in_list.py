# API in list

# copy
a = [1, 2, 3]
b = a
c = a.copy()
c[1] = 4
print(a)
b[1] = 4
print(a)

# count
['to', 'be', 'or', 'not', 'to', 'be'].count('to')
x = [[1, 2], 1, 1, [2, 1, [1, 2]]]
x.count(1)
x.count([1, 2])

# extend
a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)
a.extend(b)
print(a)

# insert
numbers = [1, 2, 3, 4, 5, 6]
numbers[3:3] = ['four']
print(numbers)
