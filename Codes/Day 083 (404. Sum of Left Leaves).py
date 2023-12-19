# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        ans = []
        stack = []
        sumLL = 0
        if root is None:
            return []

        while True:
            if root:
                stack.append(root)
                root = root.left
                if root is not None:
                    if (root.left is None) and (root.right is None):
                        sumLL += root.val

            elif stack:
                root = stack.pop()
                ans.append(root.val)
                root = root.right
            
            else:
                break
                
        return sumLL
            


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        res = 0
        if not root:
            return res
        if not root.left and not root.right:
            return res

        left_res = self.sumOfLeftLeaves(root.left)
        if root.left and not root.left.left and not root.left.right:
            res += root.left.val

        right_res = self.sumOfLeftLeaves(root.right)
        
        res += right_res
        res += left_res


        return res