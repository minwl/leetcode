# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        check = set()
        curr = head
        newhead = newcurr = ListNode()

        while curr:
            if curr.val not in check:
                check.add(curr.val)
                newcurr.next = curr
                newcurr= newcurr.next
            else:
                curr = curr.next

        newcurr.next = None

        return newhead.next