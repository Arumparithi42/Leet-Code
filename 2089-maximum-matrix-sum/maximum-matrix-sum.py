class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        c = 0
        tot = 0
        flat = [num for l in matrix for num in l]
        m = abs(flat[0])
        for i in range(len(flat)):
            if flat[i] < 0:
                c += 1
            if m > abs(flat[i]):
                m = abs(flat[i])
            tot += abs(flat[i])
        if c % 2 == 0:
            return tot
        return tot - 2 * m
        