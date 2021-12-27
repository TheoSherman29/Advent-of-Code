def parse(file):
    lines = open(file).read().split('\n')
    data = []
    for line in lines:
        (x, y) = line.split('-')
        data.append([x, y])

    return data


ex_data = parse('example.txt')
in_data = parse('input.txt')


def solve_p1(data):
    paths = []

    def move(path, cant_revisit):
        poss_caves = []
        if path[-1] == 'end':
            return path
        else:
            for connection in data:
                copy_con = connection.copy()
                if path[-1] in copy_con:
                    copy_con.remove(path[-1])
                    if copy_con[0] not in cant_revisit:
                        poss_caves.append(copy_con[0])

        for cave in poss_caves:
            if not cave.isupper():
                paths.append(move(path+[cave], cant_revisit + [cave]))
            else:
                paths.append(move(path+[cave], cant_revisit))


    move(['start'], ['start'])
    real_paths = []
    for path in paths:
        if path:
            real_paths.append(path)

    return len(real_paths)


def solve_p2(data):
    paths = []

    def move(path, cant_revisit, visit_twice):
        poss_caves = []
        if path[-1] == 'end':
            return path
        else:
            for connection in data:
                copy_con = connection.copy()
                if path[-1] in copy_con:
                    copy_con.remove(path[-1])
                    if copy_con[0] not in cant_revisit:
                        poss_caves.append(copy_con[0])
        for cave in poss_caves:
            if not cave.isupper() and visit_twice == None:
                paths.append(move(path+[cave], cant_revisit + [cave], visit_twice))
                paths.append(move(path+[cave], cant_revisit, cave))

            elif not cave.isupper() and visit_twice == cave:
                paths.append(move(path+[cave], cant_revisit + [cave], visit_twice))

            elif not cave.isupper() and visit_twice != cave:
                paths.append(move(path+[cave], cant_revisit + [cave], visit_twice))
            else:
                paths.append(move(path+[cave], cant_revisit, visit_twice))


    move(['start'], ['start'], None)
    real_paths = []
    for path in paths:
        if path and path not in real_paths:
            real_paths.append(path)

    return len(real_paths)


print(solve_p1(in_data))
print(solve_p2(in_data))