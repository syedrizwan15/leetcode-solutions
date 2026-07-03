class Solution:
    def setZeroes(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])

        MARK = float('inf')

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:

                    # row
                    for c in range(cols):
                        if matrix[i][c] != 0:
                            matrix[i][c] = MARK

                    # column
                    for r in range(rows):
                        if matrix[r][j] != 0:
                            matrix[r][j] = MARK

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == MARK:
                    matrix[i][j] = 0