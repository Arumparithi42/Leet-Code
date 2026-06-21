# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        tailA = headA
        tailB = headB
        while(tailA != None or tailB != None):
            if (tailA == None):
                tailA = headB
            if (tailB == None):
                tailB = headA
            
            if (tailA == tailB):
                return tailA
            tailA = tailA.next
            tailB = tailB.next
        return None