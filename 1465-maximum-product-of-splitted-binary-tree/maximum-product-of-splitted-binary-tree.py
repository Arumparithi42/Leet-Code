# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        allsums = []
        def tot(node):
            if not node:
                return 0
            sums = node.val + tot(node.left) + tot(node.right)
            allsums.append(sums)
            return sums
        totalsum = tot(root)
        ans = 0
        for s in allsums: 
            ans = max(ans, (totalsum - s) * s)
        return ans % (10**9 +7)