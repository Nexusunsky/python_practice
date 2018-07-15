from threading import currentThread


def fibonacci():
    a = b = 1
    yield a
    yield b
    while True:
        a, b = b, a + b
        print('fibonacci: ' + currentThread().name)
        yield b


if __name__ == '__main__':
    for num in fibonacci():
        if num > 100:
            break
        print('main: ' + currentThread().name)
        print(num, )
