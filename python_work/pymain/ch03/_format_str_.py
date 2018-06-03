from string import Template
from math import pi
from math import e

tmpl = Template("Hello, $who! $what enough for ya?")
print(tmpl.substitute(who="Mars", what="Dusty"))

# format
print("{}, {} and {}".format("first", "second", "third"))
print("{3} {0} {2} {1} {3} {0}".format("be", "not", "or", "to"))

# 关键字参数
print("{name} is approximately {value:.2f}.".format(value=pi, name="Pai"))
# 如果变量与替换字段同名，可以在字符串前面加上f
print(f"Euler`s constant is roughly {e}.")
