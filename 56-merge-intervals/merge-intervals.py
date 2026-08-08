class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x : x[0])
        cur = intervals[0]
        ans = []
        for i in range(1, len(intervals)):
            curEnd = cur[1]
            nextStart = intervals[i][0]
            nextEnd = intervals[i][1]
            if (curEnd >= nextStart):
                cur[1] = max(curEnd, nextEnd)
            else:
                ans.append(cur)
                cur = intervals[i]
        ans.append(cur)
        return ans