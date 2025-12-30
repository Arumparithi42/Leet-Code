class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        count = 0
        if row < 3 or col < 3:
            return 0
        for i in range(row - 2):
            for j in range(col - 2):
                if self.magic(grid,i,j):
                    count += 1
        return count
    def magic(self,grid,row,col):
        seen = [False] * 10
        for i in range(3):
            for j in range(3):
                e = grid[row + i][col + j]
                if e < 1 or e > 9:
                    return False
                if seen[e]:
                    return False
                seen[e] = True
        d1 = grid[row][col] + grid[row + 1][col + 1] + grid[row + 2][col + 2]
        d2 = grid[row][col + 2] + grid[row + 1][col + 1] + grid[row + 2][col]
        if d1 != d2:
            return False
        r1 = grid[row][col] + grid[row][col+1] + grid[row][col+2]
        r2 = grid[row+1][col] + grid[row + 1][col + 1] + grid[row + 1][col + 2]
        r3 = grid[row+2][col] + grid[row + 2][col +1] + grid[row + 2][col + 2]
        if d1 != r1 or r1 != r2 or r2 != r3 or r1 != r3:
            return False
        c1 = grid[row][col] + grid[row + 1][col] + grid[row + 2][col]
        c2 = grid[row][col + 1] + grid[row + 1][col + 1] + grid[row + 2][col + 1]
        c3 = grid[row][col + 2] + grid[row + 1][col + 2] + grid[row + 2][col + 2]
        if d2 != c1 or c1 != c2 or c2 != c3 or c1 != c3:
            return False
        return True