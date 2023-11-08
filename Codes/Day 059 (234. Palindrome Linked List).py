# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        picture = []

        while head:
            picture.append(head.val)
            head = head.next

        mid = len(picture) // 2
        
        return picture == picture[::-1] 






### Best Runtime Solution

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        slow = fast = head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            slow_next = slow.next
            slow.next,prev = prev,slow
            slow = slow_next
        l = prev
        r = slow if not fast else slow.next
        while l and r:
            if l.val != r.val:
                return False
            l = l.next
            r = r.next
        return True