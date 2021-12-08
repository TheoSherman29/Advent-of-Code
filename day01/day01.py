input = list(map(int, open('input.txt', 'r').read().splitlines()))
ex = list(map(int, open('example.txt', 'r').read().splitlines()))


def solve(data):
    # ans1 = 0
    # for i in range(1, len(data)):
    #     val1 = data[i-1]
    #     val2 = data[i]
    #     if val2 > val1:
    #         ans1 += 1
    vals = [[data[i-1], data[i]] for i, num in enumerate(data, 1)]
    print(vals)

    ans2 = 0
    for i in range(1, len(data)-2):
        window1 = data[i-1] + data[i] + data[i+1]
        window2 = data[i] + data[i+1] + data[i+2]
        if window2 > window1:
            ans2 += 1

    return ans2


solve(ex)