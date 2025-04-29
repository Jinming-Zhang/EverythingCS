from typing import List

'''
Use backtrack search, note the difference between backtrack search and bfs/dfs
- need to remember the current state when keep searching in next state
- if next state doesn't work, reset the variables to current state
  - i.e. reset nodes to unvisited if the path doesn't work
'''


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for r in range(len(board)):
            row = board[r]
            for c in range(len(row)):
                cell = board[r][c]
                if cell == word[0]:
                    if (self.existHelper(board, word, r, c)):
                        return True
        return False

    def existHelper(self, board: List[List[str]], word: str, r: int, c: int, visited=set()) -> bool:
        if ((r, c) in visited):
            return False
        if (len(word) == 1 and board[r][c] == word[0]):
            return True

        curVisited = set(visited)
        curVisited.add((r, c))
        nextWord = word[1:]

        nextR = r-1
        if nextR >= 0 and board[nextR][c] == word[1]:
            if (self.existHelper(board, nextWord, nextR, c, curVisited)):
                return True
        nextR = r+1
        if nextR < len(board) and board[nextR][c] == word[1]:
            if (self.existHelper(board, nextWord, nextR, c, curVisited)):
                return True
        nextC = c - 1
        if nextC >= 0 and board[r][nextC] == word[1]:
            if (self.existHelper(board, nextWord, r, nextC, curVisited)):
                return True
        nextC = c+1
        if nextC < len(board[r]) and board[r][nextC] == word[1]:
            if (self.existHelper(board, nextWord, r, nextC, curVisited)):
                return True

        return False


inputs = []
board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCB"
inputs.append([board, word])
board = [["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]]
word = "ABCESEEEFS"
inputs.append([board, word])
board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCCED"
inputs.append([board, word])
board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "SEE"
inputs.append([board, word])
print([Solution().exist(inp[0], inp[1]) for inp in inputs])
