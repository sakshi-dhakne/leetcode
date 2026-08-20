# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        def zigzag(root):
            result = []
            queue = deque([])
            queue.append(root)
            if root == None:
                return []
            while len(queue) != 0:
                level = len(queue)
                curr = []
                for _ in range(level):
                    e = queue.popleft()
                    curr.append(e.val)
                    if e.left != None:
                        queue.append(e.left)
                    if e.right != None:
                        queue.append(e.right)
                    
                if len(result)%2==1:
                    curr.reverse()
                result.append(curr)
            
            return result

        return (zigzag(root))