def parse(file):
    return open(file, 'r').read().strip().split('\n')


ex_data = parse('example.txt')
in_data = parse('input.txt')


def surrounding(data, x, y):
    poss_vals = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
    vals = [(xi, yi) for (xi, yi) in poss_vals if 0 <= xi < len(data[0]) and 0 <= yi < len(data)]
    return vals


def is_min(data, x, y):
    for (xi, yi) in surrounding(data, x, y):
        if data[yi][xi] <= data[y][x]:
            return False
    return True


def solve_p1(data):
    sum = 0
    for y, row in enumerate(data):
        for x, num in enumerate(row):

            if is_min(data, x, y):
                sum += (1 + int(data[y][x]))
    return sum


def solve_p2(data):
    str_data = data
    data = []
    for row_i, row in enumerate(str_data):
        basin_row = []
        for num_i, num in enumerate(row):
            if num != '9':
                basin_row.append(0)
            else:
                basin_row.append(1)
        data.append(basin_row)
    print(data)
    basins = []

    def find_size(x, y):
        if x < 0 or y < 0 or x > len(data[0]) - 1 or y > len(data) - 1 or data[y][x] == 1:
            return
        data[y][x] = 1
        print(x, y, data)
        basins[-1] += 1
        find_size(x+1, y)
        find_size(x-1, y)
        find_size(x, y+1)
        find_size(x, y-1)

    for row_i, row in enumerate(data):
        for num_i, num in enumerate(row):
            basins.append(0)
            find_size(num_i, row_i)

    sorted_basins = sorted(basins, reverse=True)
    return sorted_basins[0] * sorted_basins[1] * sorted_basins[2]


print(solve_p1(in_data))
print(solve_p2(in_data))