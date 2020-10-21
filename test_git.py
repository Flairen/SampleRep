def simple_print():
    print('Hello!')


def summ(*args):
    s = 0
    for arg in args:
        s += arg
    return s

if __name__ == '__main__':
    simple_print()
    print(summ(5, 7, 8))

