# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        forward=fast=curr=head
        prev=next=None
        while fast and fast.next:
            #find middle node
            fast = fast.next.next
            forward = forward.next
            
            #reverse until middle node
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            
        #if list is odd, move forward start position     
        if fast and not fast.next:
            forward = forward.next
        
        #reverse traverse    
        reverse = prev
        while forward:
            if reverse.val != forward.val:
                return False
            else:
                reverse = reverse.next
                forward = forward.next
        if reverse == forward == None:
            return True
        
            
            
            