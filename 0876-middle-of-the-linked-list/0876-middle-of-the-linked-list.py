# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        curr = head
        count = 0
        while curr is not None:
            count += 1
            curr = curr.next
        
        mid = count//2
        point = head
        steps = 0
        while steps < mid:
            steps += 1
            point = point.next 

        return point



