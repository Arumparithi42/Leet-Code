from collections import defaultdict
import itertools 
class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        T = defaultdict(list)
        for row in allowed:
            T[(row[0], row[1])].append(row[2])
        m = {}
        def solve(row):
            if len(row) == 1:
                return True
            if row in m:
                return m[row]
            option = []
            for i in range(len(row) - 1):
                key = (row[i], row[i+1])
                if key in T:
                    option.append(T[key])
                else:
                    m[row] = False
                    return False
            for nrow in itertools.product(*option):
                if solve("".join(nrow)):
                    m[row] = True
                    return True
            m[row] = False
            return False
        return solve(bottom)