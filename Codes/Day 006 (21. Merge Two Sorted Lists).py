# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        L1 = []
        while list1:
            L1.append(list1.val)
            list1 = list1.next
        L2 = []
        while list2:
            L2.append(list2.val)
            list2 = list2.next
        #print(L1,L2)

        L = sorted(L1 + L2,reverse=True)
        #print(L)
        
        prev = None
        ans = None
        for item in L:
            ans = ListNode(val = item, next = prev)
            prev = ans

        return ans

