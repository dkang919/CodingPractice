# very poor solution ...

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return None
        
        L = []

        while head:
            L.append(head.val)
            head = head.next

        ans = ListNode(val=L[0])

        for v in L[1:]:
            ans = ListNode(val=v, next=ans)

        return ans


# Best and Classic Method

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        new_list = None
        current = head

        while current:
            next_node = current.next
            current.next = new_list
            new_list = current
            current = next_node

        return new_list