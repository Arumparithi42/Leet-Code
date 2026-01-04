class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        s = 0
        for num in nums:
            c = 0
            t = 0
            for i in range(1, int(num**0.5) + 1):
                if num % i == 0:
                    c += 1
                    t += i
                    if i*i != num:
                        c += 1
                        t += num // i
                    if c > 4:
                        break
            if c == 4:
                s += t
        return s