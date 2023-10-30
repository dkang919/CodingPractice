# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        L = []

        while head:
            if head.val != val:
                L.append(ListNode(val=head.val, next = None))
            head = head.next 

        size = len(L)
        
        if size == 0:
            return None

        for i in range(len(L)-1):
            L[i].next = L[i+1]

        return L[0]


### One of the core

## remove potential head with val
## reference head with new variable cur 
## let cur delete vals 
## then return head 

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head and head.val == val:
            head = head.next
        cur = head

        while cur and cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head