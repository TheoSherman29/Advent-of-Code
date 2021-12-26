def parse(file):
    return open(file).read().split('\n')

ex_data = parse('example.txt')
in_data = parse('input.txt')

pairs = {'(': ')', '[': ']', '{': '}', '<': '>'}
scoreKey1 = {')': 3, ']': 57, '}': 1197, '>': 25137}
scoreKey2 = {'(': 1, '[': 2, '{': 3, '<': 4}


def solve_p1(data):
    def chunk(row, openChunks, i):
        if i == len(row):
            return None

        elif row[i] in pairs.keys():
            return chunk(row, openChunks+[row[i]], i+1)

        elif row[i] == pairs[openChunks[-1]]:
            return chunk(row, openChunks[:-1], i+1)

        else:
            return row[i]

    score = 0
    for row_i, row in enumerate(data):
        ans = chunk(row, [], 0)
        if ans != None:
            score += scoreKey1[ans]

    return score


def solve_p2(data):

    def chunk(row, openChunks, i):
        if i == len(row):
            score = 0
            for char in reversed(openChunks):
                score *= 5
                score += scoreKey2[char]
            return score

        elif row[i] in pairs.keys():
            return chunk(row, openChunks+[row[i]], i+1)

        elif row[i] == pairs[openChunks[-1]]:
            return chunk(row, openChunks[:-1], i+1)

        else:
            return None

    scores = []
    for row_i, row in enumerate(data):
        ans = chunk(row, [], 0)
        if ans != None:
            scores.append(ans)

    print(scores)
    midScore = sorted(scores)[int(len(scores)/2)]

    return midScore


print(solve_p1(in_data))
print(solve_p2(in_data))
