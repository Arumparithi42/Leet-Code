# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        l = set()
        tail = head
        while(tail != None):
            if (tail in l):
                return True
            l.add(tail)
            tail = tail.next
        return False

        