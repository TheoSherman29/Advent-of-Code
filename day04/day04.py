def intify(str):
    int_lst = []
    for i in str:
        int_lst.append(int(i))
    return int_lst

def parse(file_name):
    with open(file_name) as f:
        data = f.read().split('\n\n')
        str_nums, str_boards = data[0].split(','), data[1:]

    draws = []
    for num in str_nums:
        draws.append(int(num))
    board_rows = []
    for board in str_boards:
        for row in board.splitlines():
            row = row.replace('  ', ' ')
            board_rows.append(intify(row.split()))

    boards = []
    board = []
    counter = 0
    for row_i, row in enumerate(board_rows):
        counter += 1
        board.append(row)
        if counter == 5:
            counter = 0
            boards.append(list(board))
            board = []

    checks = [[[False for _ in range(5)] for _ in range(5)] for _ in boards]

    return draws, boards, checks


ex_draws, ex_boards, ex_checks = parse('example.txt')
in_draws, in_boards, in_checks = parse('input.txt')


def is_winner(check):
    columns = [True for _ in range(5)]
    for r in range(5):
        good_row = True
        for d in range(5):
            if not check[r][d]:
                good_row = False
                columns[d] = False
        if good_row: return True
    return any(columns)


def game_p1(boards, checks, draws):
    for draw in draws:
        for board_i, board in enumerate(boards):
            for row_i, row in enumerate(board):
                for num_i, num in enumerate(row):
                    if num == draw:
                        checks[board_i][row_i][num_i] = True
                        if is_winner(checks[board_i]):
                            return get_score(board, checks[board_i], draw)


def game_p2(boards, checks, draws):
    wins = [False for _ in boards]
    for draw in draws:
        for board_i, board in enumerate(boards):
            for row_i, row in enumerate(board):
                for num_i, num in enumerate(row):
                    if num == draw:
                        checks[board_i][row_i][num_i] = True
                        if is_winner(checks[board_i]):
                            wins[board_i] = True
            if all(wins): return get_score(board, checks[board_i], draw)


def get_score(winner, check, draw):
    sum = 0
    for row in range(5):
        for col in range(5):
            if not check[row][col]: sum += winner[row][col]
    return sum * int(draw)


print(game_p1(in_boards, in_checks, in_draws))
print(game_p2(in_boards, in_checks, in_draws))
