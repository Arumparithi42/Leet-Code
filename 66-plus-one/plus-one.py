class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        sum = 0
        l = len(digits)
        for i in range(l):
            sum += digits[i] * pow(10,l-1)
            l -= 1
        sum += 1
        sum = str(sum)
        li = []
        for i in sum:
            li.append(int(i))
        return li