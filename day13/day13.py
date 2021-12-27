def parse(file):
    points_str, instructions_str = open(file).read().strip().split('\n\n')

    points_lst = points_str.split('\n')
    instructions_lst = instructions_str.split('\n')

    points = []
    for point in points_lst:
        [x, y] = point.split(',')
        points.append([x, y])

    instructions = []
    for line in instructions_lst:
        fold, along, instr = line.split(' ')
        dir, coord = instr.split('=')

        instructions.append((dir, coord))


    return points, instructions


ex_points, ex_instructions = parse('example.txt')
in_points, in_instructions = parse('input.txt')


def findMax(points):
    maxx = 0
    maxy = 0
    for point in points:
        if int(point[0]) > maxx:
            maxx = int(point[0])
        if int(point[1]) > maxy:
            maxy = int(point[1])

    return maxx, maxy


maxx_ex, maxy_ex = findMax(ex_points)
maxx_in, maxy_in = findMax(in_points)
print(maxx_in, maxy_in)

def solve(points, instructions, maxx, maxy):
    data = [[0 for _ in range(maxx)] for _ in range(maxy)]
    for [x, y] in points:
        data[int(y)][int(x)] = 1

    def fold(data, instruction, width, height):
        new_data = data.copy()
        fold_line = int(instruction[-1])
        if instruction[0] == 'x':
            for yi in range(height):
                for xi in range(width-fold_line):
                    if data[yi][xi+fold_line] == 1:
                        new_data[yi][fold_line-xi] = 1
                new_data[yi] = new_data[yi][:fold_line]

        elif instruction[0] == 'y':
            for yi in range(height-fold_line):
                for xi in range(width):
                    if data[yi+fold_line][xi] == 1:
                        new_data[fold_line-yi][xi] = 1
            new_data = new_data[:fold_line]


        # for line in new_data:
        #     print(line)

        return new_data

    folded1 = fold(data, instructions[0], maxx, maxy)

    folded = data.copy()
    for inst in instructions:
        old = folded
        folded = fold(old, inst, len(old[0]), len(old))

    res1 = 0
    for row in folded1:
        for dot in row:
            if dot == 1:
                res1 += 1

    return res1


print(solve(ex_points, ex_instructions, maxx_ex+1, maxy_ex+1))
print(solve(in_points, in_instructions, maxx_in+1, maxy_in+1))