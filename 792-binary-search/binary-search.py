class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0; right = len(nums) - 1
        while(left <= right):
            mid = (left+right)//2 # (rigth - left)/2 + left
            if (target < nums[mid]):
                right = mid - 1
            elif (nums[mid] < target):
                left = mid + 1
            else: 
                return mid
        return -1
