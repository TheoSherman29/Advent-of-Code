input = open('input.txt', 'r').read().strip().split(',')
ex = open('example.txt', 'r').read().strip().split(',')


def solve(strdata):
    data = []
    for i in range(len(strdata)):
        data.append(int(strdata[i]))

    fuels1 = []
    for i in range(len(data)):
        fuels1.append(0)
        for crab in data:
            fuels1[i] += abs(i - crab)

    fuels2 = []
    for i in range(len(data)):
        fuels2.append(0)
        for crab in data:
            distance = abs(i - crab)
            fuels2[i] += int(distance * (distance + 1) / 2)


    return min(fuels1), min(fuels2)


print(solve(ex))