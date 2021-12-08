from collections import Counter

input = open('input.txt', 'r').read().splitlines()


def solve(lst, o2=True):
    length, pv, diff, new_lst = len(lst[0]), 0, 0, []
    while pv < length:
        for num in lst:
            if num[pv] == '1':
                diff += 1
            else:
                diff += -1
        if o2:
            if diff >= 0:
                tie = '1'
            else:
                tie = '0'
        else:
            if diff >= 0:
                tie = '0'
            else:
                tie = '1'
        for num in lst:
            if num[pv] == tie:
                new_lst.append(num)
                print(diff, new_lst)
        if len(new_lst) == 1:
            return new_lst[0]
        lst = new_lst
        diff = 0
        pv += 1
        new_lst = []


o2 = solve(input)
co2 = solve(input, False)


print(o2, co2 ,int(o2, 2) * int(co2, 2))