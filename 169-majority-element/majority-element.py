class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        l = len(nums)//2
        d = {}
        for num in nums:
            d[num] = d.get(num, 0) + 1
            if (d.get(num) > l):
                return num
       