class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows
        currRow = 0
        down = True

        for ch in s:
            rows[currRow] += ch

            if currRow == 0:
                down = True
            elif currRow == numRows - 1:
                down = False

            if down:
                currRow += 1
            else:
                currRow -= 1

        return "".join(rows)