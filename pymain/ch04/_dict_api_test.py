from copy import deepcopy

# copy的 浅拷贝和深拷贝
x = {'username': 'admin', 'machines': ['foo', 'bar', 'baz']}
y = x.copy()
y['username'] = 'mlh'
y['machines'].remove('bar')
print(y)
print(x)

d = {'names': ['Alfred', 'Bertrand']}
c = d.copy()
dc = deepcopy(d)
d['names'].append('Clive')
print(c)
print(dc)

# fromkeys 创建一个新字典，其中包含一个指定的键
print({}.fromkeys('name', 'age'))
print({}.fromkeys(['name', 'age'], "unknown"))

d = {'title': 'Python Web Site', 'url': 'http://www.python.org', 'spam': 0}
d_items = d.items()
print(d_items)
