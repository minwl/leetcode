# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        if not head: return None
        if not head.next.next : return head.val+head.next.val

        twinmax=float('-inf')
        #go to middle and spread out (similar to find palindrom)
        fast=slow=head
        prev = None
        
        while fast and fast.next:
            fast = fast.next.next
            #reverse half of the list 
            next = slow.next
            slow.next = prev
            prev = slow
            slow = next

        while prev and slow:

            twinmax = max(twinmax, prev.val+slow.val)
            prev = prev.next
            slow = slow.next

        return twinmax



