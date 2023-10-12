# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []

        ans = []
        self.traversal(root,ans)

        return ans 

    def traversal(self, t: Optional[TreeNode], tlist: list) -> List[int]:

        if not t:
            return []
            
        else:
            self.traversal(t.left,tlist)
            self.traversal(t.right,tlist)
            tlist.append(t.val)