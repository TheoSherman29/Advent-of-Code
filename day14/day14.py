from collections import Counter
from functools import lru_cache


def parse(file):
    template, rules = open(file).read().split('\n\n')
    rules_lst = rules.split('\n')

    rules = {}
    for rule in rules_lst:
        pair, new = rule.split(' -> ')
        rules[pair] = new

    return template, rules


ex_temp, ex_rules = parse('example.txt')
in_temp, in_rules = parse('input.txt')


def solve_p1(temp, rules, steps):
    poly = temp
    n = 0
    while n < steps:
        new_poly = ''
        for i, char in enumerate(poly):
            if i+1 < len(poly):
                new_poly = new_poly + char + rules[char+poly[i+1]]
            else:
                new_poly = new_poly + poly[-1]

        poly = new_poly
        n += 1

    counts = {}
    for char in poly:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1

    return max(counts.values()) - min(counts.values())


def solve_p2(temp, rules, steps):
    @lru_cache(maxsize=None)
    def insert(pair, steps):
        if steps == 0: return Counter()

        new_char = rules[pair]
        left = pair[0] + new_char
        right = new_char + pair[1]
        counter = Counter(new_char)

        counter.update(insert(left, steps-1))
        counter.update(insert(right, steps-1))

        return counter

    ans = Counter(temp)
    for i in range(len(temp)-1):
        pair = temp[i:i+2]
        ans.update(insert(pair, steps))

    return max(ans.values()) - min(ans.values())


print(solve_p1(in_temp, in_rules, 10))
print(solve_p2(in_temp, in_rules, 40))