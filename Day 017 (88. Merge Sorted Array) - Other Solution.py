# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        L = []

        while head:
            if head.val not in L:
                L.append(head.val)
            head = head.next

        prev = None
        ans = None
        for item in L[-1::-1]:
            ans = ListNode(val = item, next = prev)
            prev = ans

        return ans
