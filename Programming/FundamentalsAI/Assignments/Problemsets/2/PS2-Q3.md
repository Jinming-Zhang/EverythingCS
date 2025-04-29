# Jinming Zhang
## Problem #3
Result are from the minimax search alrorithm.
#### Board 1
Utility value 1001, best move at (2,2), bottom-right

#### Board 2
Utility value 0, best move at (0,0), top-left

#### Board 3
Utility value 4, best move at (1,1), middle

#### Python script
```py
# define player
x = 'x'
o = 'o'

# define boards in question
board_1 = [
    [x, o, o],
    [x, x, o],
    [None, None, None]
]
board_2 = [
    [None, x, None],
    [None, o, o],
    [None, x, None]
]

board_3 = [
    [None, None, None],
    [None, None, None],
    [None, None, None]
]


def deep_clone_board(original):
    new_board = []
    for row in original:
        new_board.append([c for c in row])
    return new_board

# get empty grids/available actions for given board


def get_empty_position(b):
    available_positions = []
    for r in range(0, len(b)):
        for c in range(0, len(b)):
            if b[r][c] == None:
                available_positions.append((r, c))
    return available_positions

# get score for Maximus given a list representing row/col/diagonal


def get_list_score(lst):
    mscore = 0
    x_count = 0
    o_count = 0
    for player in lst:
        if player == x:
            x_count += 1
        if player == o:
            o_count += 1
    if x_count == 3:
        mscore += 1000
    elif o_count == 3:
        mscore -= 1000
    else:
        mscore += (x_count - o_count)
    return mscore


def get_terminal_value(b):
    maxi_score = 0
    # row score
    for row in b:
        maxi_score += get_list_score(row)
    # col score
    for i in range(0, 3):
        col = [r[i] for r in b]
        maxi_score += get_list_score(col)
    # diagonal score
    dia1 = [b[0][0], b[1][1], b[2][2]]
    maxi_score += get_list_score(dia1)
    dia2 = [b[0][2], b[1][1], b[2][0]]
    maxi_score += get_list_score(dia2)
    return maxi_score


def minimax_start(board):
    result = minimax(board, True)
    return result


def minimax(state, isMax):
    '''
    return best action and current util value
    '''
    current_board = deep_clone_board(state)
    available_actions = get_empty_position(current_board)
    if(len(available_actions) == 0):
        return [get_terminal_value(current_board), None]

    # initialize score
    current_score = None
    if(isMax):
        current_score = -999999
    else:
        current_score = 9999999

    # search through possible sub states
    best_action = None
    for action in available_actions:
        r, c = action
        next_board = deep_clone_board(current_board)
        if(isMax):
            next_board[r][c] = x
        else:
            next_board[r][c] = o

        score, _ = minimax(next_board, (not isMax))

        if(isMax):
            if score > current_score:
                current_score = score
                best_action = action
        else:
            if(score < current_score):
                current_score = score
                best_action = action
    return [current_score, best_action]


print(minimax_start(board_1))
print(minimax_start(board_2))
print(minimax_start(board_3))

```