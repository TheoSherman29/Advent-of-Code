def parse(file):
    return [[int(x) for x in row] for row in open(file).read().split('\n')]


ex_data = parse('example.txt')


def solve_p1(data):
    visited = [[0 for _ in range(len(data[0]))] for _ in range(len(data))]

    