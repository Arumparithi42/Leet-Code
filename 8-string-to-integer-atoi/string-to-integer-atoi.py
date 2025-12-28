class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        sign = 1
        n = '0'
        if s == "":
            return 0
        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]
        for i in s:
            if i.isdigit():
                n += i
            else:
                break
        n = int(n)*sign
        if sign == 1 and n > 2**31 - 1:
            n = 2**31 -1
        if sign == -1 and n < -2**31:
            n = -2**31
        return n