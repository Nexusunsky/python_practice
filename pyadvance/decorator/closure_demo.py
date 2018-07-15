import inspect


def closureFunc(up):
    val = 0

    def nestedFunc(arg):
        nonlocal val
        print("Welcome To Closure ")
        for i in range(up + 1):
            val += i
        val *= arg
        print("Total is =  %d" % val)

    return nestedFunc


if __name__ == '__main__':
    retFunc = closureFunc(5)
    tps = retFunc.__closure__

    for it in tps:
        print(it)

    print(inspect.getclosurevars(closureFunc))
    print(inspect.getclosurevars(retFunc))
    print(len(retFunc.__closure__))
    print(type(retFunc.__closure__))
    print(retFunc.__closure__[0].cell_contents)
    print(retFunc.__closure__[1].cell_contents)

    retFunc(10)
    print(retFunc.__closure__)
    print(retFunc.__closure__[0].cell_contents)
    print(retFunc.__closure__[1].cell_contents)

    retFunc(4)
    print(retFunc.__closure__)
    print(retFunc.__closure__[0].cell_contents)
    print(retFunc.__closure__[1].cell_contents)
