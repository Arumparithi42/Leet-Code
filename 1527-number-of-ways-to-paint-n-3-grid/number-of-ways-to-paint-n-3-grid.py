class Solution:
    def numOfWays(self, n: int) -> int:
        abc = 6
        aba = 6
        mod = 10**9 + 7
        for _ in range(n - 1):
            nabc = (2 * abc + 2 * aba) % mod
            naba = (3 * aba + 2 * abc) % mod
            abc = nabc
            aba = naba
        return (aba + abc) % mod