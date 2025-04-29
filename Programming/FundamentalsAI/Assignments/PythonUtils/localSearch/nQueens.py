import random
from typing import List


class nQueens:
    def __init__(self, n=8) -> None:
        self.board = []
        self.n = n
        self.get_random_initial_state()

    def get_random_initial_state(self) -> None:
        for i in range(0, self.n):
            self.board.append(random.randint(0, self.n-1))

    def get_attacking_pairs(self, board):
        attacking_pairs = []
        # check column
        queens_in_column = []
        for col in range(0, len(board)):
            queens = 0
            for row in range(0, len(board)):
                if board[row] is col:
                    queens += 1
            queens_in_column.append(queens)
        total_attacking_queens_in_column = sum(
            [x > 1 for x in queens_in_column])
        # check row
        # check diagonal
        pass

    def print_board(self) -> str:
        res = ""
        for row in range(0, self.n):
            rowStr = ""
            for j in range(0, self.n):
                if self.board[row] is not j:
                    rowStr = rowStr + " _ "
                else:
                    rowStr = rowStr + " Q "
            rowStr += "\n"
            res += rowStr
        print(res)
        return res


def deep_clone(lst):
    return [x for x in lst]


def evaluate_state(state: List[int]):
    '''
    state: [1,2,1,2,4]
    len(state) = n, for n queens problem
    range(state) = [1,n], inclusive
    '''
    attacking_pairs = 0
    cp = deep_clone(state)
    # attacking row pairs
    unique = list(dict.fromkeys(cp))
    attacking_pairs += (len(state)-len(unique))

    # attacking diagonal pairs
    for i in range(0, len(state)-1):
        curr = state[i]
        next = state[i+1]
        if abs(curr-next) == 1:
            attacking_pairs += 1
    return attacking_pairs


def climb(initial_state: List[int]):
    n = len(initial_state)
    possible_values = range(1, n+1)
    current_state = deep_clone(initial_state)
    current_score = evaluate_state(current_state)
    iter_count = 1
    while(True):
        print("iteration: "+str(iter_count))
        next_candidate = deep_clone(current_state)
        next_candidate_score = current_score

        for i in range(0, n):
            value = current_state[i]
            actions = deep_clone(possible_values)
            actions.remove(value)
            for action in actions:
                next = deep_clone(current_state)
                next[i] = action
                next_score = evaluate_state(next)
                print("\t next possible state : ",
                      str(next)+", score: "+str(next_score))
                if(next_score < next_candidate_score):
                    next_candidate = deep_clone(next)
                    next_candidate_score = next_score
        if next_candidate_score < current_score:
            current_state = deep_clone(next_candidate)
            current_score = next_candidate_score
            print("find a better solution: " + str(current_state) +
                  ", score: "+str(current_score))
        else:
            print("no better solution found, returning current solution")
            break
        iter_count += 1
    return current_state


print(evaluate_state([1, 2, 1, 2, 4]))
print(climb([1, 2, 1, 2, 4]))
