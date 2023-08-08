# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:        
        head = ListNode()
        ans = 0
        ten = 1
        while l1 or l2:
            if not l1 : 
                val = l2.val * ten
            elif not l2 : 
                val = l1.val * ten
            else : val = (l1.val + l2.val)*ten
            ans += val
            if l1 : 
                l1 = l1.next
            if l2:
                l2 = l2.next
            ten *= 10
        
        ans = str(ans)
        i = len(ans)-1
        currNode = head
        while i >= 0:
            val = int(ans[i])
            currNode.val = val
            if i != 0:
                currNode.next = ListNode()
            currNode = currNode.next
            i -= 1
        return head