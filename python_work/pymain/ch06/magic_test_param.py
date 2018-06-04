def story(**kwargs):
    return 'Once upon a time ,there was a ' \
           '{job} called {name}.'.format_map(kwargs)


def power(x, y, *others):
    if others:
        print('Received redundant parameters:', others)
    return pow(x, y)


def interval(start, stop=None, step=1):
    """Imitates rang() for step > 0 """
    if stop is None:
        start, stop = 0, start
    result = []

    i = start
    while i < stop:
        result.append(i)
        i += step
    return result


def multiplier(factor):
    def multiplyByFactory(number):
        return number * factor

    return multiplyByFactory


if __name__ == '__main__':
    params = {'job': 'language', 'name': 'Python'}
    del params['job']
    print(story(job='stroke of genius', **params))
    print(interval(3, 12, 4))
    print(power(*interval(3, 7)))
    print(multiplier(2)(3))
