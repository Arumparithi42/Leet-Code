# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        tail = head
        delete = head
        for _ in range(n):
            tail = tail.next
        if (tail == None):
            return head.next
        while(tail.next):
            tail = tail.next
            delete = delete.next
        delete.next = delete.next.next
        return head