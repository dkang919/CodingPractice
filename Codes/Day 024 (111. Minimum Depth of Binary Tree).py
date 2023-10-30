# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        if (not root.left) or (not root.right):
            return max(self.minDepth(root.left), self.minDepth(root.right)) + 1

        else:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1




# Best runtime solution 

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = []
        def bfs(node):
            queue.append(node)
            count = 0
            while queue:
                count +=1
                for i in range(len(queue)):
                    curr = queue.pop(0)
                    
                    if curr.left:
                        queue.append(curr.left)
                    if curr.right:
                        queue.append(curr.right)
                    if curr.left is None and curr.right is None:
                        return count
            return count
        return bfs(root)