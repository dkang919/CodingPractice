# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        bucket = set()
        currentA = headA
        currentB = headB

        while currentA:
            if currentA not in bucket:
                bucket.add(currentA)

            currentA = currentA.next

        while currentB:
            if currentB in bucket:
                return currentB
                
            currentB = currentB.next
        
        return None
        

# hashset consumes more memory than list, but runtime is much faster as the size of data increases


## other solution

# either they will be crossed at intersection or None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a, b = headA, headB

        while(a != b):
            a = headB if a is None else a.next
            b = headA if b is None else b.next
        
        return a