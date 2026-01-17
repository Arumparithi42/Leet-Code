class Solution:
    def maxArea(self, height: List[int]) -> int:
        m = 0
        l = 0
        h = len(height)-1
        while l < h:
            area = min(height[l],height[h]) * (h-l)
            if area > m:
                m = area
            if height[l] > height[h]:
                h -= 1
            else:
                l += 1
        return m