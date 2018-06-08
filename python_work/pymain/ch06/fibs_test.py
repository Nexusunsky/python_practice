fibs = [0, 1]
for i in range(8):
    fibs.append(fibs[-2] + fibs[-1])

print(fibs)


def fib_num(num):
    """Define a fib num of the num. """
    result = [0, 1]
    for i in range(num - 2):
        result.append(result[-2] + result[-1])
    return result


print(fib_num(10))
print(fib_num.__doc__)
help(fib_num)
