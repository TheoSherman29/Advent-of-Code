def parse(file):
    return open(file).read().split('\n')


ex_data = parse('example.txt')
in_data = parse('input.txt')


def explode(num):
    if type(num[0]) is int and type(num[1]) is int:
        pass
    elif type(num[0]) is int and type(num[1]) is list:
        num[0] + explode(num[1])

    elif type(num[0]) is list and type(num[1]) is int:

        explode(num[0])
