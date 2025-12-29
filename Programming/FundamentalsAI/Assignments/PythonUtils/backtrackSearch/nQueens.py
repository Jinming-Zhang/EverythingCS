# class nQueens:
#     def __init__(self, board) -> None:
#         self.board = board


# n = 8
# board_empty_cell = " _ "
# board_queen_cell = " Q "
# row = [board_empty_cell for i in range(n)]
# board = []
# for i in range(0, n):
#     board.append([board_empty_cell for i in range(n)])

import random


schedule = [
    [2, 4, 1, 8, 6, 9, 3, 7, 5],
    [7, 2, 3, 1, 9, 4, 5, 6, 8],
    [1, 5, 2, 8, 6, 9, 7, 4, 3],
    [6, 7, 3, 1, 8, 9, 2, 5, 4],
    [7, 1, 6, 3, 9, 4, 8, 5, 2],
    [3, 1, 6, 4, 8, 9, 2, 5, 7],
]


def getCount(lst):
    rowCount = {}
    colCount = {}
    for coord in lst:
        # row
        row, col = coord
        if row not in rowCount:
            rowCount[row] = 1
        else:
            rowCount[row] = rowCount[row] + 1
        # col
        if col not in colCount:
            colCount[col] = 1
        else:
            colCount[col] = colCount[col] + 1
    return [rowCount, colCount]


def satisfy(lst):
    rowCount = {}
    colCount = {}
    for coord in lst:
        # row
        row, col = coord
        if row not in rowCount:
            rowCount[row] = 1
        else:
            rowCount[row] = rowCount[row] + 1
        if rowCount[row] != 3:
            return False
        # col
        if col not in colCount:
            colCount[col] = 1
        else:
            colCount[col] = colCount[col] + 1
        if (colCount[col] != 2):
            return False
    return True


def getAvailableCell(current):
    '''
    current: [(1,2)...]
    '''
    rowCount, colCount = getCount(current)
    result = []
    for r in range(0, len(schedule)):
        row = schedule[r]
        for c in range(0, len(row)):
            cell = row[c]
            if (rowCount[r] < 3 and colCount[c] < 3):
                result.append((r, c))
    return result


def getRandomInitial():
    initial = []
    for r in range(0, len(schedule)):
        rowSolution = []
        allActions = getAvailableCell(initial)
        allactionsinRow = [x for x in allActions if x[0] == r]
        while len(rowSolution) != 3:
            rand = random.randint(0, len(allactionsinRow)-1)
            elmt = allactionsinRow[rand]
            rowSolution.append(elmt)
            allactionsinRow.remove(elmt)
        for can in rowSolution:
            initial.append(can)
    return initial


i1 = getRandomInitial()

maxScore = 0
