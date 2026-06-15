class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        while(j < n):
            if (i == m + j):
                nums1[i] = nums2[j]
                i = i + 1
                j = j +1
                continue
            if (nums1[i] <= nums2[j]):
                i = i + 1
            else :
                for k in range(m+n-1,i-1,-1):
                    nums1[k] = nums1[k-1]
                nums1[i] = nums2[j]
                j = j + 1
                i = i + 1