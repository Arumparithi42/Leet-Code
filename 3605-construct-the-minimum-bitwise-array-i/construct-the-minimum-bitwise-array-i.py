class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for x in nums:
            for i in range(1, x):
                if (i | (i+1)) == x:
                    ans.append(i)
                    break
            else:
                ans.append(-1) 
        return ans