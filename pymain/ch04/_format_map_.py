# 使用字符串格式设置功能来设置值的格式
# 这些值是作为命名或非命名参数提供给方法format
# 而通过字典进行格式设置将变得更容易

phoneBook = {'Beth': '9102', 'Alice': '2341', 'Cecil': '3258'}
print("Cecil's phone number is {Cecil}.".format_map(phoneBook))

template = '''<html> 14 
... <head><title>{title}</title></head>
... <body>
... <h1>{title}</h1>
... <p>{text}</p>
... </body>'''

data = {'title': 'My Home Page', 'text': 'Welcome to my home page!'}
print(template.format_map(data))

x = {}
y = x
x['key'] = 'value'
print(y)
x = {}  # x 指向了一个新的dict
print(x)
print(y)


