from typing import List


'''
Transpose then switch columns
'''
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for r in range(n):
            for c in range(r):
                tmp = matrix[r][c]
                matrix[r][c] = matrix[c][r]
                matrix[c][r] = tmp

        for c in range(int(n/2)):
            for r in range(n):
                tmp = matrix[r][c]
                matrix[r][c] = matrix[r][n-c-1]
                matrix[r][n-c-1] = tmp


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Solution().rotate(matrix)
print(matrix)
