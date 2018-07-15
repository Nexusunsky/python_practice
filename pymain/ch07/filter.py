class Filter(object):
    def __init__(self):
        self.blocked = []

    def filter(self, sequence):
        targets = [x for x in sequence if x not in self.blocked]
        print(targets)
        return targets


class SPAMFilter(Filter):
    def __init__(self):
        super().__init__()
        self.blocked = ['SPAM']


if __name__ == '__main__':
    filter = Filter()
    filter.filter([1, 2, 3])
    print(filter.__class__)

    filter = SPAMFilter()
    filter.filter(['SPAM', 'SPAM', 'SPAM', 'eggs', 'bacon', 'SPAM'])

    print(issubclass(SPAMFilter, Filter))
    print(SPAMFilter.__bases__)
    print(Filter.__bases__)
    print(filter.__class__)
