>>> print(repr("Hello,\nWorld!"))
'Hello,\nWorld!'
>>> print(str("Hello,\nWorld!"))
Hello,
World!
>>> path = "C:\nowhere"
>>> print(path)
C:
owhere
>>> path = "C:\\nwhere"
>>> print(path)
C:\nwhere
>>> print(r"This is illegal")
This is illegal
>>> print(r"This is illegal\")
  File "<stdin>", line 1
    print(r"This is illegal\")
                             ^
SyntaxError: EOL while scanning string literal
>>> print(r"This is illegal\\")
This is illegal\\
>>> print(r"This is illegal" "\\")
This is illegal\
>>> 