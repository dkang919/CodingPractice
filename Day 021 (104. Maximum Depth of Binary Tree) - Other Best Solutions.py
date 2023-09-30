#-----------------------------------------------------------
#  Best Memory Solution
#-----------------------------------------------------------
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
    # DFS iteratively
        if not root:
            return 0

        height = 0
        q = deque([root])
        while q:
            cur_length = len(q)
            for el in range(cur_length):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            height += 1
        return height

    
    
    '''
    # DFS recursively
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    '''

# Idea is using quque structure to use DFS, it may not be too fast, but highly effective in memory use - no need to update variables by recursion


#-----------------------------------------------------------
#  Best Runtime Solution
#-----------------------------------------------------------

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        
        return max(left_depth, right_depth) + 1


# no longer need helper function since it would not require additional params
# recursion with + 1