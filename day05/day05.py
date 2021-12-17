def parse(file):
    lines = open(file).read().split('\n')
    coords = []
    for line in lines:
        (x1, y1), (x2, y2) = [tuple(int(i) for i in xy.strip().split(',')) for xy in line.strip().split('->')]
        coords.append(((x1, y1), (x2, y2)))
    return(coords)


ex_coords = parse('example.txt')
in_coords = parse('input.txt')


def solve_p1(coords):

    vents = [[0 for _ in range(1000)] for _ in range(1000)]
    for line in coords:
        x1, y1, x2, y2, = line[0][0], line[0][1], line[1][0], line[1][1]
        if x1 == x2:
            for y in range(abs(y2 - y1) + 1):
                vents[y + min(y1, y2)][x1] += 1
        elif y1 == y2:
            for x in range(abs(x2 - x1) + 1):

                vents[y1][x + min(x1, x2)] += 1
    ans = 0
    for row_1, row in enumerate(vents):
        for vent_i, vent in enumerate(row):
            if vent >= 2:
                ans += 1

    return ans


def solve_p2(coords):
    vents = [[0 for _ in range(1000)] for _ in range(1000)]
    for line in coords:
        x1, y1, x2, y2, = line[0][0], line[0][1], line[1][0], line[1][1]
        if x1 == x2:
            for y in range(abs(y2 - y1) + 1):
                vents[y + min(y1, y2)][x1] += 1
        elif y1 == y2:
            for x in range(abs(x2 - x1) + 1):
                vents[y1][x + min(x1, x2)] += 1
        elif (y2 > y1 and x2 > x1) or (y2 < y1 and x2 < x1):
            for x in range(abs(x2 - x1) + 1):
                vents[x + min(y1, y2)][x + min(x1, x2)] += 1
        else:
            for x in range(abs(x2 - x1) + 1):
                vents[max(y1, y2) - x][min(x1, x2) + x] += 1

    ans = 0
    print(vents)
    for row_1, row in enumerate(vents):
        for vent_i, vent in enumerate(row):
            if vent >= 2:
                ans += 1

    return ans

print(solve_p1(in_coords))
print(solve_p2(in_coords))
