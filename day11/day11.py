def parse(file):
    str_data = open(file).read().split('\n')
    data = []
    for row in str_data:
        new_row = []
        for val in row:
            new_row.append(int(val))
        data.append(new_row)

    return data


ex_data = parse('example.txt')
in_data = parse('input.txt')

data = in_data
flashes = 0
flashed = [[False for _ in row] for row in data]

def surrounding(x, y):
    poss_vals = []
    for px in range(x-1, x+2):
        for py in range(y-1, y+2):
            if x != px or y != py:
                poss_vals.append((px, py))
    vals = [(xi, yi) for (xi, yi) in poss_vals if 0 <= xi < len(data[0]) and 0 <= yi < len(data)]
    return vals


def flashSurrounding(surrPoints):
    global flashes
    #print(surrPoints)
    for (x, y) in surrPoints:
        data[y][x] += 1
        #print((x, y), data)

    for (x, y) in surrPoints:
        if data[y][x] > 9 and flashed[y][x] == False:
            #print(data[y][x])
            #print((x, y), data[y][x])
            flashed[y][x] = True
            flashes += 1
            print((x, y))
            print(flashed)
            flashSurrounding(surrounding(x, y))


def solve_p1():
    n = 0
    global flashes, flashed
    while True:

        for row_i, row in enumerate(data):
            for val_i, val in enumerate(row):
                data[row_i][val_i] += 1

        for row_i, row in enumerate(data):
            for val_i, val in enumerate(row):
                if val > 9 and flashed[row_i][val_i] == False:
                    #print((val_i, row_i), val)
                    flashed[row_i][val_i] = True
                    flashes += 1
                    print((val_i, row_i))
                    print(flashed)
                    flashSurrounding(surrounding(val_i, row_i))

        for row_i, row in enumerate(flashed):
            for val_i, val in enumerate(row):
                if val == True:
                    data[row_i][val_i] = 0

        sync = True
        for row in flashed:
            for val in row:
                if val == False: sync = False

        if sync == True:
            return  n + 1
        flashed = [[False for _ in row] for row in data]
        #print(data, flashed)
        n += 1


print(solve_p1())
