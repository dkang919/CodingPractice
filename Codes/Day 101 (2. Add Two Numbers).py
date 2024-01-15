# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        L1 = ""
        L2 = ""

        while l1:
            L1 = str(l1.val) + L1
            l1 = l1.next

        while l2:
            L2 = str(l2.val) + L2
            l2 = l2.next

        if len(L1) == len(L2):
            pass
        
        elif len(L1) >= len(L2):
            diff = len(L1) - len(L2)
            L2 = "0"*diff + L2
    
        else: 
            diff = len(L2) - len(L1)
            L1 = "0"*diff + L1

        L = str(int(L1) + int(L2))

        N = None
        for n in L:
            N = ListNode(n, next=N)
            
        return N