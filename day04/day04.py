import sys
import pathlib


def intify(str):
    int_lst = []
    for i in str:
        int_lst.append(int(i))
    return int_lst


with open('example.txt') as f:
    data = f.read().split('\n\n')
    ex_nums, ex_boards = data[0].split(','), data[1:]
    form_ex_nums = []
    for num in ex_nums:
        form_ex_nums.append(int(num))
    form_ex_boards = []
    for board in ex_boards:
        for row in board.splitlines():
            row = row.replace('  ', ' ')
            form_ex_boards.append(intify(row.split()))
    board_counter = 0
    reform_ex_boards = []
    print(form_ex_boards)
    for row in range(len(form_ex_boards)):
        reform_ex_boards.append([])
        counter = 0
        while counter < 5:
            reform_ex_boards[board_counter].append(form_ex_boards[row])
            counter += 1
        board_counter += 1

print(reform_ex_boards)
form_ex_boards = dict(zip(range(len(reform_ex_boards)), reform_ex_boards))
boards = form_ex_boards

bingo_boards = {}
for board in boards:
    new_board = []
    for row in boards[board]:
        new_row = []
        for num in row:
            new_row.append([num, False])
        new_board.append(new_row)
    bingo_boards[board] = new_board


for i in range(len(form_ex_nums)):
    for board in bingo_boards:
        for row in bingo_boards[board]:
            for num in row:
                if form_ex_nums[i] == num[0]:
                    num[1] = True
    for board in bingo_boards:
        for row in bingo_boards[board]:
            winner = board
            for i in range(5):
                if row[i][1] == False:
                    winner = None
        for i in range(5):
            winner = board
            for j in range(5):
                if bingo_boards[board][j][i][1] == False:
                    winner = None
            if winner:
                print(bingo_boards[board])
                break
        if winner:
            break
    if winner:
        break

#