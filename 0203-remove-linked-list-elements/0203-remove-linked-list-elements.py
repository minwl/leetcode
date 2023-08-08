# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """

        if not head:
            return None
        newhead = ListNode()
        curr = head
        newcurr = newhead
        while curr:
            if curr.val != val:
                newcurr.next = curr
                curr = curr.next
                newcurr = newcurr.next
            else:
                curr = curr.next
        newcurr.next = None
        return newhead.next


