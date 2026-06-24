class Solution:
    def reverseBits(self, n: int) -> int:
        a = []
        while(n != 0):
            a.append(n%2)
            n //= 2
        for i in range(len(a),32):
            a.append(0)
        tot = 0
        p = 0
        for i in range(len(a)-1,-1,-1):
            tot += a[i]*2**p
            p+=1
        return tot