# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        return self.height(root) != -1

    def height(self, node):
        if not node:
            return 0

        lh = self.height(node.left)
        if lh == -1:
            return -1 

        rh = self.height(node.right)
        if rh == -1:
            return -1

        if abs(lh-rh) > 1:
            return -1

        return max(lh,rh) + 1


# Solution by priyanshu11_
# Approach 

# Create a helper function to calculate the height of the subtree rooted at a given node - let it calculate and return -1 if it's not height balanced


