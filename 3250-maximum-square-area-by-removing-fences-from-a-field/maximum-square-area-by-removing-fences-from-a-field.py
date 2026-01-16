class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        h = set()
        v = set()
        hFences.extend([1,m])
        hFences.sort()
        for i in range(len(hFences)):
            for j in range(i):
                h.add(hFences[i] - hFences[j])
        vFences.extend([1,n])
        vFences.sort()
        for i in range(len(vFences)):
            for j in range(i):
                v.add(vFences[i] - vFences[j])
        com = v & h
        if not com:
            return -1
        return max(com)**2 % (10**9 + 7)