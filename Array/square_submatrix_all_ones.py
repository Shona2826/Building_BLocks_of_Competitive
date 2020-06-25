class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        count = 0
        count = sum(matrix[0])+sum([row[0] for row in matrix[1:]])
        for i in range(1,n):
            for j in range(1,m):
                if matrix[i][j] == 1:
                    matrix[i][j] = 1 + min(matrix[i-1][j],matrix[i][j-1],matrix[i-1][j-1])
                    count +=matrix[i][j]
        return count   