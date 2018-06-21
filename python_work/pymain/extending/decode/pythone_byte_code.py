import dis


def to_python_decode(file=''):
    binary_io = open('%s' % file, 'rb')
    fd = binary_io.read()
    co = compile(fd, file, 'exec')
    dis.dis(co)
    binary_io.close()


if __name__ == '__main__':
    file = '/Users/haoliu/Documents/Project/TWWorkSpace/delivery-infrastructure/app/tdp/service/planet/command.py'
    to_python_decode(file)

    # dis.dis(__confirm_island_and_portal_cleared)
