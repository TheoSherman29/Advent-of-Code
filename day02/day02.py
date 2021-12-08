input = open('input.txt', 'r').read().split('\n')
ex = open('example.txt', 'r').read().split('\n')


def solve(data):
    xpos1 = 0
    depth1 = 0
    for i in range(0, len(data) - 1):
        if data[i][0] == 'f':
            xpos1 += int(data[i][-1])
        elif data[i][0] == 'd':
            depth1 += int(data[i][-1])
        elif data[i][0] == 'u':
            depth1 -= int(data[i][-1])

    xpos2 = 0
    depth2 = 0
    aim = 0
    for i in range(0, len(data)-1):
        if data[i][0] == 'f':
            xpos2 += int(data[i][-1])
            depth2 += (aim * int(data[i][-1]))
        elif data[i][0] == 'd':
            aim += int(data[i][-1])
        elif data[i][0] == 'u':
            aim -= int(data[i][-1])

    return xpos1 * depth1, xpos2 * depth2