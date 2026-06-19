class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s = []
        
        for num in nums:
            if num not in s:
                s.append(num)
                
            else:
                s.remove(num)
        return s[0]