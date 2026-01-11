class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        rows, cols = len(matrix), len(matrix[0])
        height = [0] * (cols + 1)
        maxarea = 0
        for row in matrix:
            for i in range(cols):
                if row[i] == '1':
                    height[i] += 1
                else:
                    height[i] = 0
            stack = [-1]
            for i in range(cols +1):
                while stack[-1] != -1 and height[stack[-1]] >= height[i]:
                    h = height[stack.pop()]
                    w = i - stack[-1] - 1
                    maxarea = max(maxarea, h*w)
                stack.append(i)
        return maxarea
        