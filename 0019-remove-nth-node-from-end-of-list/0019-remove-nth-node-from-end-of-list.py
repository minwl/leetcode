# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        len = 0
        while curr:
            curr = curr.next
            len += 1
        if len == n:
            head = head.next
            return head
        prev = None
        curr = head
        while curr:
            prev = curr
            curr = curr.next
            len -= 1
            if len == n:
                prev.next = curr.next
                break
        return head