# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        plist = []
        qlist = []
        self.traverse(p,plist)
        self.traverse(q,qlist)
        print(plist, qlist)
        return plist == qlist

    def traverse(self, t: Optional[TreeNode], tlist: list) -> None:
        if not t:
            tlist.append("Null")
            return

        self.traverse(t.left,tlist)
        self.traverse(t.right,tlist)
        tlist.append(t.val)

    # idea came from the previous question's best solution 
    # as the domain/complexity of this question is not heavy, recursive approach will be efficient
    # implemented helper function "traverse" to simplify the approach
    # require more practice on fundamental skills of data structure and algorithm
