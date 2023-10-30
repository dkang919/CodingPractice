# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        if root.left:
            ldepth = self.travel(root.left)
        else:
            ldepth = 1

        if root.right:
            rdepth = self.travel(root.right)
        else:
            rdepth = 1
            
        return max(ldepth, rdepth)


    def travel(self, t: Optional[TreeNode]):

        if not t:
            return 1
        else:
            return max(self.travel(t.left)+1, self.travel(t.right)+1)