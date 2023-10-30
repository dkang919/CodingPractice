# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        left = []
        right = []
        self.traverse(root.left, "L", left)
        self.traverse(root.right, "R", right)

        return left == right  
        
    def traverse(self, subroot, direction, subroot_list) -> None:
        if not subroot:
            subroot_list.append("Null")
            return
        
        if direction == "L":
            self.traverse(subroot.left,"L",subroot_list)
            self.traverse(subroot.right,"R",subroot_list)
            subroot_list.append(subroot.val)
            
        elif direction == "R":
            self.traverse(subroot.right,"R",subroot_list)
            self.traverse(subroot.left,"L",subroot_list)
            subroot_list.append(subroot.val)


# used the idea of the previous problem 
# successful on memory use, but poor performance in runtime speed