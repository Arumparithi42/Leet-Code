class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        maxy = 0
        totarea = 0
        for x, y, l in squares:
            totarea += l * l
            maxy = max(maxy, y + l)
        def check(ylimit):
            area = 0
            for x, y, l in squares:
                if y <= ylimit:
                    area += l * min(ylimit - y, l)
            return area >= totarea/2
        l, h = 0, maxy
        e = 1e-5
        while abs(h - l) >= e:
            mid = (l+h)/2
            if check(mid):
                h = mid
            else:
                l = mid
        return h