import dis


def main():
    list1 = []
    list2 = None
    if list1:
        print('empty list')
    else:
        print('None')
    if list2:
        print('empty list')
    else:
        print('None')


if __name__ == '__main__':
    main()
    dis.dis(main)
