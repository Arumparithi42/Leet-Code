class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        r = len(grid)
        c = len(grid[0])
        i = r - 1
        j = 0
        count = 0
        while i >= 0 and j < c:
            if grid[i][j] < 0:
                count += c - j
                i -= 1
            else:
                j += 1
        return count