# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []

        ans = [root.val]

        plist = []
        qlist = []
        self.traverse(root.left,plist)
        self.traverse(root.right,qlist)

        return ans + plist + qlist

    def traverse(self, t: Optional[TreeNode], tlist: list) -> None:
        if not t:
            return []

        tlist.append(t.val)
        self.traverse(t.left,tlist)
        self.traverse(t.right,tlist)