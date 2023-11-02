## Solution by trpaslik


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def heightL(node): # height along left edge 
            ans = 0
            while node:
                node = node.left
                ans += 1
            return ans
        def heightR(node): # height along right edge 
            ans = 0
            while node:
                node = node.right
                ans += 1
            return ans
        h = heightL(root)
        if h == 0:
            return 0
        hm = heightR(root.left) + 1  # height in the mid (along right edge of left subtree)
        if h == hm:
            # Left subtree is full, right is complete
            return (1 << (h-1)) + self.countNodes(root.right)
        else:
            # Right subtree is full, left subtree is complete
            return self.countNodes(root.left) + (1 << (hm-1))