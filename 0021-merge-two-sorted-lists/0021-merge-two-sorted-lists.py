# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head = cur = ListNode()

        while list1 and list2:
            if list1.val <= list2.val :
                cur.next = ListNode(list1.val)
                list1 = list1.next
                cur = cur.next
            else :
                cur.next = ListNode(list2.val)
                list2 = list2.next
                cur = cur.next
        if list1 or list2:
            if list1:
                cur.next = list1
            else : 
                cur.next = list2
        return head.next