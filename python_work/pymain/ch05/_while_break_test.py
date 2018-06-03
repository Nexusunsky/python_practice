from math import sqrt

word = input('Please enter a word: ')
while word:
    print('The word was ', word)
    word = input('Please enter a word: ')

# if/break行将整个循环分成两部分:
# 第一部分负责设置(如果使 用常规while循环，将重复这部分)，
# 第二部分在循环条件为真时使用第一部分初始化的数据。
while True:
    word = input('Please enter a word: ')
    if not word:
        break
    print('The word was ', word)

# 在循环中添加一条else子句，它仅在没有调用break时才执行。
for n in range(99, 81, -1):
    root = sqrt(n)
    if root == int(root):
        print(n)
        break
else:
    print("Didn't find it!")
