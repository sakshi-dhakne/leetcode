# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        curr = head
        count = 0
        prev = None
        while curr is not None:
                count += 1
                prev = curr
                curr = curr.next
            
        pos = count - n
        curr = head
        if pos == 0:
            return curr.next

        steps = 0
        prev = None
        while curr.next is not None and steps < pos:
            prev = curr
            curr = curr.next
            steps +=1
            
        prev.next = curr.next
        return head
                  
            
            
               