# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        mid = self.findmid(head)
        left = self.sortList(head)
        right = self.sortList(mid)
        return self.merge(left, right)
        
    def findmid(self, head):
        fast=head
        slow=None
        while fast and fast.next:
            fast = fast.next.next
            if not slow:
                slow = head
            else: slow = slow.next
        mid = slow.next
        slow.next = None
        return mid
    
    def merge(self, left, right):
        dummyhead = ListNode()
        dummy = dummyhead
        while left and right:
            if left.val < right.val:
                dummy.next = left
                left = left.next
            else:
                dummy.next = right
                right = right.next
            dummy = dummy.next
        if left : 
            dummy.next = left
        else:
            dummy.next = right
        return dummyhead.next
                
                