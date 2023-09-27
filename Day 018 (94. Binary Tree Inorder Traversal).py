# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        stack = []
        if root is None:
            return []

        while True:
            if root:
                stack.append(root)
                root = root.left
                
            elif stack:
                root = stack.pop()
                ans.append(root.val)
                root = root.right
            
            else:
                break
                
        return ans


# recursion can be a better option since the complexity of the problem is very low.
