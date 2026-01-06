# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = collections.deque()
        q.append(root)
        m = float('-inf')
        ans, level = 0,0
        while q:
            level += 1
            csum = 0
            for _ in range(len(q)):
                node = q.popleft()
                csum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if m < csum:
                ans = level
                m = csum
        return ans